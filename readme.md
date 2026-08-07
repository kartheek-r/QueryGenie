# 🧞 QueryGenie

> An AI-powered **Natural Language to SQL** application built with **Google Gemini and SQLite** that converts plain English questions into SQL queries and instantly retrieves database results.

---

## 📌 Project Overview

Writing SQL takes time, even for people who know it well — and it's a hard barrier for anyone who doesn't. QueryGenie removes that barrier: type a question in plain English, and it generates the correct SQL query, runs it against a live SQLite database, and returns the results — no SQL knowledge required.

---

## ✨ Features

- 💬 Ask database questions in **plain English**
- 🤖 **AI-powered SQL generation** using Google Gemini
- 🗄️ Executes queries live against a **SQLite** database
- 📊 Instant, readable results — no manual query writing
- 🖥️ Simple, interactive **Streamlit** UI

---

## 🏗️ How It Works

```
User asks a question in English
        ↓
Gemini  →  Converts question into a SQL query using schema context
        ↓
SQLite  →  Executes the generated SQL query
        ↓
Results displayed in Streamlit UI
```

---

## 🛠️ Tech Stack

| Component        | Technology           |
|-------------------|-----------------------|
| 🖥️ Frontend / UI  | Streamlit             |
| 🤖 AI Model        | Google Gemini         |
| 🗄️ Database        | SQLite                |
| 🔐 Env Management  | python-dotenv         |

---

## 📂 Project Structure

```
QueryGenie/
│
├── app.py              # Main Streamlit application
├── sqlite.py           # Database connection & query execution
├── student.db           # Sample SQLite database
├── requirements.txt     # Python dependencies
├── .gitignore
└── README.md
```

---

## 🖼️ Project UI

*Add a screenshot of the app here, e.g.:*
`![QueryGenie UI](./assets/querygenie-ui.jpeg)`

---

## ▶️ How to Run Locally

### 1. Clone the Repository

```bash
git clone https://github.com/kartheek-r/QueryGenie.git
cd QueryGenie
```

### 2. Create a Virtual Environment

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Set Up API Key

Create a `.env` file in the root folder:

```
GOOGLE_API_KEY=your_google_gemini_api_key_here
```

> 🔑 Get your free API key at [Google AI Studio](https://aistudio.google.com/)

### 5. Run the App

```bash
streamlit run app.py
```

---

## 💬 Sample Questions

- Show all students
- Show students with marks greater than 85
- Count total students
- Display student names in descending order

---

## 💡 Use Cases

- 📊 Non-technical users querying a database without learning SQL
- 🎓 Students learning how natural language maps to SQL
- ⚡ Quick ad-hoc data lookups without opening a query editor

---

## 🔮 Future Improvements

- 🗂️ Support for multiple/custom databases
- ✅ SQL query validation before execution
- 🕘 Query history
- 📥 Export results to CSV

---

## 🙌 Conclusion

QueryGenie combines **prompt engineering** and **schema-aware SQL generation** to turn plain English into working database queries — a practical demonstration of applying LLMs to structured data access.

---

## 👨‍💻 Author

**Ryalampadu Kartheek**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/kartheek-ryalampadu) [![Gmail](https://img.shields.io/badge/Gmail-D14836?style=flat-square&logo=gmail&logoColor=white)](mailto:kartheekryalampadu@gmail.com) [![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/kartheek-r)
