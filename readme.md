# QueryGenie

An AI-powered Natural Language to SQL Query Generator Using Google Gemini and SQLite

## Features

- Convert English questions into SQL
- Uses Google Gemini API
- SQLite database
- Streamlit web interface
- Easy to use

## Tech Stack

- Python
- Streamlit
- SQLite
- Google Gemini API

## Project Structure

```
NLP2SQL/
│── app.py
│── sqlite.py
│── requirements.txt
│── .env
│── student.db
│── README.md
```

## Installation

```bash
git clone https://github.com/your-username/nlp2sql-gemini.git
cd nlp2sql-gemini
pip install -r requirements.txt
```

Create a `.env` file:

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

Run the application:

```bash
streamlit run app.py
```

## Sample Questions

- Show all students
- Show students with marks greater than 85
- Count total students
- Display student names in descending order

## Future Improvements

- Support multiple databases
- SQL query validation
- Query history
- Export results to CSV

## Author

Karthik