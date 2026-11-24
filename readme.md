# 🧞 QueryGenie

🔗 **Live Demo:** https://querygenie-r8llvbbfg3zjsvkeqx9egh.streamlit.app/

> Ask a database question in plain English. An **AI agent** built on Google Gemini reads the schema, writes SQL, runs it safely, and fixes its own errors, with every step visible.

---

## 📌 Overview

Writing SQL is a barrier for anyone who doesn't know it. QueryGenie removes that barrier, and it does it with an **agent** instead of a single prompt. Gemini is given two tools, decides when to use them, sees the results of its own queries, and corrects itself when a query fails.

## ✨ Features

- 💬 Ask questions in **plain English**
- 🛠️ **Tool calling:** Gemini calls `get_schema()` and `run_sql()` on its own
- 🧠 **Schema understanding:** table structure is read from the database automatically, not hard-coded
- 🔁 **Self-correction loop:** if a query fails, the error goes back to the model, which fixes the SQL and retries (up to 4 attempts)
- 🛡️ **Guardrails:** only a single read-only `SELECT` is allowed, writes are blocked, and the database opens in read-only mode
- 📊 Results as a table, plus an automatic bar chart when the data fits
- 🔍 **Agent steps** panel showing every SQL attempt and its outcome
- ☁️ Deployed on Streamlit Cloud

## 🏗️ How It Works

```
User question (English)
        ↓
Gemini 3.5 Flash (function calling)
   ├─ get_schema()  → reads CREATE TABLE statements from SQLite
   └─ run_sql(query)
         ├─ Guardrail: single SELECT only, blocked keywords rejected
         ├─ Executes on a read-only SQLite connection
         └─ Returns rows, or the error message
        ↓
Error? → model reads it, fixes the SQL, retries (max 4 attempts)
        ↓
Answer + SQL + results table + chart + agent steps
```

## 🛠️ Tech Stack

| Component | Technology |
|---|---|
| UI | Streamlit |
| LLM | Google Gemini 3.5 Flash (`google-genai` SDK, function calling) |
| Database | SQLite (opened read-only) |
| Data handling | pandas |
| Hosting | Streamlit Cloud |

## 📂 Project Structure

```
QueryGenie/
├── app.py             # Streamlit app + agent loop + guardrails
├── sqlite.py          # Sample database setup
├── student.db         # Sample SQLite database (STUDENT table)
├── requirements.txt
└── readme.md
```

## 🖼️ Screenshots

**Question answered with SQL and results**

![QueryGenie answer](1000384443.jpg)

**Guardrail refusing a delete request**

![Guardrail](1000384444.jpg)



## 💬 Try These Questions

- Show students with marks greater than 85
- Count total students
- Display student names in descending order of marks
- Delete all students *(refused by the guardrail)*

## ▶️ Run Locally

**1. Clone the repo**
```bash
git clone https://github.com/kartheek-r/QueryGenie.git
cd QueryGenie
```

**2. Create a virtual environment**
```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Add your API key**

Get a free key from [Google AI Studio](https://aistudio.google.com/), then create `.streamlit/secrets.toml`:
```toml
GOOGLE_API_KEY = "your_key_here"
```
(Or set an environment variable named `GOOGLE_API_KEY`.)

**5. Run**
```bash
streamlit run app.py
```

## ☁️ Deploy on Streamlit Cloud

1. Push the repo to GitHub
2. Go to [share.streamlit.io](https://share.streamlit.io) → **Create app**
3. Select the repo, branch `main`, main file `app.py`
4. Under **Advanced settings → Secrets**, add `GOOGLE_API_KEY = "your_key_here"`
5. Deploy

## ⚠️ Limitations

- Works with the included sample database (`student.db`)
- The guardrail uses a keyword blocklist plus a read-only connection, which is good for a demo but not a full SQL security layer
- Results are capped at 100 rows
- The model can still write a wrong query; the retry loop fixes errors, not wrong-but-valid logic

## 🔮 Future Improvements

- Upload or connect your own database (PostgreSQL / MySQL)
- Schema retrieval for large databases (embed table descriptions and fetch only relevant ones)
- Query history and CSV export
- An evaluation set to measure query accuracy

## 👨‍💻 Author

**Ryalampadu Kartheek**
[LinkedIn](https://www.linkedin.com/in/kartheek-ryalampadu) · [GitHub](https://github.com/kartheek-r)
