import streamlit as st
import sqlite3
import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

prompt = """
You are an expert in converting English questions into SQL queries.
The SQL database has one table named STUDENT with the following columns:
NAME, CLASS, SECTION, MARKS.

Return ONLY the SQL query.
Do not include markdown, explanations, or ```sql.
"""

def get_gemini_response(question):
    response = model.generate_content([prompt, question])
    return response.text.strip()

def read_sql_query(sql):
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    conn.close()
    return rows

st.set_page_config(page_title="NLP2SQL")

st.title("🧠 NLP to SQL using Gemini")

question = st.text_input("Ask a question about the student database")

if st.button("Generate SQL"):
    sql_query = get_gemini_response(question)

    st.subheader("Generated SQL")
    st.code(sql_query, language="sql")

    try:
        result = read_sql_query(sql_query)

        st.subheader("Result")
        st.write(result)

    except Exception as e:
        st.error(f"Error: {e}")