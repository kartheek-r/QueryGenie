import os
import re
import sqlite3
import pandas as pd
import streamlit as st
from google import genai
from google.genai import types

MODEL = "gemini-3.5-flash"
DB_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "student.db")
MAX_ATTEMPTS = 4
BLOCKED = re.compile(
    r"\b(insert|update|delete|drop|alter|create|replace|attach|detach|pragma|vacuum|reindex)\b",
    re.I,
)

st.set_page_config(page_title="QueryGenie", page_icon="🧞")
st.title("🧞 QueryGenie")
st.caption(
    "Ask in English. The AI agent reads the schema, writes SQL, runs it safely, "
    "and fixes its own errors."
)


def get_api_key():
    try:
        return st.secrets["GOOGLE_API_KEY"]
    except Exception:
        return os.getenv("GOOGLE_API_KEY")


api_key = get_api_key()
if not api_key:
    st.error("Set GOOGLE_API_KEY in Streamlit Secrets or as an environment variable.")
    st.stop()

client = genai.Client(api_key=api_key)

LOG = []


def connect():
    return sqlite3.connect(f"file:{DB_PATH}?mode=ro", uri=True)


def get_schema() -> str:
    """Return the CREATE TABLE statements for every table in the database."""
    con = connect()
    try:
        rows = con.execute(
            "SELECT sql FROM sqlite_master "
            "WHERE type='table' AND name NOT LIKE 'sqlite_%'"
        ).fetchall()
    finally:
        con.close()
    return "\n".join(r[0] for r in rows if r[0])


def run_sql(query: str) -> dict:
    """Run one read-only SQLite SELECT query. Returns columns and rows, or an error message to fix."""
    attempt = {"sql": query, "ok": False, "error": None, "df": None}
    LOG.append(attempt)

    if len(LOG) > MAX_ATTEMPTS:
        attempt["error"] = "Attempt limit reached."
        return {"error": "Attempt limit reached. Stop and explain what went wrong."}

    q = query.strip().rstrip(";").strip()
    if not re.match(r"^(select|with)\b", q, re.I) or ";" in q or BLOCKED.search(q):
        attempt["error"] = "Blocked by guardrail: only a single read-only SELECT is allowed."
        return {"error": attempt["error"]}

    try:
        con = connect()
        try:
            cur = con.execute(q)
            cols = [d[0] for d in cur.description]
            rows = cur.fetchmany(100)
        finally:
            con.close()
    except Exception as e:
        attempt["error"] = str(e)
        return {"error": str(e)}

    attempt["ok"] = True
    attempt["df"] = pd.DataFrame(rows, columns=cols)
    return {"columns": cols, "rows": [list(r) for r in rows]}


SYSTEM = f"""You are a careful SQLite data analyst.
Always call get_schema first, then write one SELECT query and call run_sql.
If run_sql returns an error, read it, fix the query, and call run_sql again
(at most {MAX_ATTEMPTS} attempts in total).
Never modify data. After you get results, answer the question in one or two plain sentences.
If the request asks to change or delete data, refuse and explain that this app is read-only."""

question = st.text_input(
    "Ask a question about the database",
    placeholder="e.g. Show students with marks greater than 85",
)

if st.button("Ask", type="primary") and question.strip():
    LOG.clear()
    with st.spinner("Thinking..."):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=question,
                config=types.GenerateContentConfig(
                    system_instruction=SYSTEM,
                    tools=[get_schema, run_sql],
                    temperature=0,
                ),
            )
        except Exception as e:
            st.error(f"Gemini error: {e}")
            st.stop()
    st.session_state["out"] = {
        "answer": response.text or "",
        "attempts": list(LOG),
    }

out = st.session_state.get("out")
if out:
    ok = [a for a in out["attempts"] if a["ok"]]

    st.subheader("Answer")
    st.write(out["answer"] or "No answer returned.")

    if ok:
        last = ok[-1]
        st.code(last["sql"], language="sql")
        st.dataframe(last["df"])
        df = last["df"]
        if (
            len(df.columns) == 2
            and len(df) > 1
            and pd.api.types.is_numeric_dtype(df.iloc[:, 1])
        ):
            st.bar_chart(df.set_index(df.columns[0]))

    with st.expander(f"Agent steps ({len(out['attempts'])} SQL attempt(s))"):
        for i, a in enumerate(out["attempts"], 1):
            status = "✅ success" if a["ok"] else f"❌ {a['error']}"
            st.markdown(f"**Attempt {i}:** {status}")
            st.code(a["sql"], language="sql")
