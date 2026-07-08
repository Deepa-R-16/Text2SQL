# AI Text-to-SQL Application

## Overview

AI Text-to-SQL Application is an AI-powered system that converts natural language questions into SQL queries and executes them on a relational database.

The application allows users to interact with databases using simple English questions instead of writing SQL manually. It uses Large Language Models (LLMs) to understand user queries, generate SQL commands, retrieve data from PostgreSQL, and provide human-readable answers.

---

## Features

- Convert natural language questions into SQL queries
- Execute generated SQL queries on PostgreSQL database
- Support conversational database interaction
- Generate AI-based explanations for query results
- Handle filtering, aggregation, grouping, and data retrieval operations
- Export query results into CSV format

---

## Tech Stack

- **Programming Language:** Python
- **Database:** PostgreSQL
- **AI/LLM:** Gemini API
- **Framework:** LangChain
- **Data Processing:** Pandas
- **Environment Management:** Python Virtual Environment (venv)

---

## Architecture

```
User Question
      |
      ↓
Large Language Model (LLM)
      |
      ↓
SQL Query Generation
      |
      ↓
PostgreSQL Database
      |
      ↓
Query Result Processing
      |
      ↓
AI Generated Response
```

---

## Project Structure

```
Text2SQL/
│
├── app.py
├── database.py
├── llm.py
├── vector_search.py
├── memory.py
│
├── datasets/
│   ├── users.csv
│   ├── products.csv
│   ├── orders.csv
│   ├── order_items.csv
│   ├── reviews.csv
│   └── events.csv
│
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
```

Navigate to the project folder:

```bash
cd Text2SQL
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate virtual environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Setup

Create a `.env` file and add your API key:

```
GEMINI_API_KEY=your_api_key_here
```

Configure your PostgreSQL database connection details in the project.

---

## Running the Application

Activate the virtual environment:

```bash
venv\Scripts\activate
```

Run:

```bash
python app.py
```

Enter a database question when prompted.

Example:

```
Ask your database question: Show all users
```

The application generates SQL, executes it, and displays the result.

---

## Example Queries

Examples of supported questions:

- Show all users
- Show all female users
- How many users are there?
- How many users are from each city?
- Show all products

---

## Future Improvements

- Add advanced conversational memory
- Improve SQL query validation
- Add web-based user interface
- Support multiple database systems
- Deploy the application as a cloud service

---

## Author

Deepa R

AI & Machine Learning Student