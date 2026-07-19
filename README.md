# 🤖 AI Text-to-SQL Assistant

An AI-powered Text-to-SQL web application that converts natural language questions into PostgreSQL SQL queries using Google's Gemini AI and executes them on a PostgreSQL database. The application displays the generated SQL, query results, and an AI-generated explanation in an interactive web interface.

---

## 🌐 Live Demo

### Frontend
https://text2sql-ruby.vercel.app/

### Backend (FastAPI)
https://text2sql-a5mj.onrender.com

### API Documentation
https://text2sql-a5mj.onrender.com/docs

---

# 📌 Project Overview

Traditional databases require users to know SQL syntax to retrieve information. This project allows users to interact with the database using plain English.

Example:

**User Input**

> Show all Female users

↓

**Generated SQL**

```sql
SELECT *
FROM users
WHERE gender='Female';
```

↓

**Database Result**

Returns all female users from the PostgreSQL database.

↓

**AI Explanation**

Provides a human-readable explanation of the query result.

---

# 🚀 Features

- Convert Natural Language to SQL using Gemini AI
- PostgreSQL Database Integration
- AI Generated SQL Queries
- AI Generated Query Explanation
- Database Statistics Dashboard
- Query Execution Time
- SQL Copy Button
- Export Results to CSV
- Export Results to Excel
- Export Results to JSON
- Responsive User Interface
- FastAPI Backend
- React Frontend
- REST API
- Swagger API Documentation
- Fully Deployed Online

---

# 🛠 Tech Stack

## Frontend

- React.js
- HTML5
- CSS3
- JavaScript
- Axios

## Backend

- Python
- FastAPI
- Uvicorn

## Database

- PostgreSQL

## AI

- Google Gemini 2.5 Flash

## Deployment

- Render (Backend)
- Vercel (Frontend)

---

# 📂 Project Structure

```
Text2SQL
│
├── backend
│   ├── main.py
│   ├── database.py
│   ├── schema.py
│   ├── sql_generator.py
│   ├── answer_generator.py
│   ├── requirements.txt
│   └── .env
│
├── frontend
│   ├── src
│   │   ├── App.jsx
│   │   ├── App.css
│   │   └── components
│   │
│   ├── public
│   └── package.json
│
└── README.md
```

---

# ⚙️ System Architecture

```
User

   │

   ▼

React Frontend

   │

REST API

   │

FastAPI Backend

   │

Gemini AI

   │

Generate SQL

   │

PostgreSQL Database

   │

Execute Query

   │

Return Results

   │

Generate AI Explanation

   │

Display Results
```

---

# 🗄 Database Tables

The project contains six tables.

## Users

- user_id
- name
- email
- gender
- city
- signup_date

## Products

- product_id
- product_name
- category
- brand
- price
- rating

## Orders

- order_id
- user_id
- order_date
- total_amount
- status

## Order Items

- order_item_id
- order_id
- product_id
- quantity
- price

## Reviews

- review_id
- user_id
- product_id
- rating
- review_text

## Events

- event_id
- user_id
- event_name
- event_time

---

# 📊 Dataset

| Table | Records |
|--------|---------|
| Users | 10,000 |
| Products | 2,000 |
| Orders | 20,000 |
| Order Items | 50,000+ |
| Reviews | 15,000+ |
| Events | 10,000+ |

---

# 🔑 Environment Variables

Create a `.env` file inside the backend.

```
DB_HOST=your_host
DB_PORT=5432
DB_NAME=text2sql
DB_USER=postgres
DB_PASSWORD=your_password

GEMINI_API_KEY=your_api_key
```

---

# ▶️ Installation

## Clone Repository

```bash
git clone https://github.com/Deepa-R-16/Text2SQL.git
```

```
cd Text2SQL
```

---

## Create Virtual Environment

Windows

```bash
python -m venv venv
```

Activate

```bash
venv\Scripts\activate
```

---

## Install Backend Packages

```bash
pip install -r requirements.txt
```

---

## Run Backend

```bash
uvicorn main:app --reload
```

Backend

```
http://127.0.0.1:8000
```

Swagger

```
http://127.0.0.1:8000/docs
```

---

## Run Frontend

```bash
cd frontend
```

```bash
npm install
```

```bash
npm run dev
```

---

# 📡 API Endpoints

## Home

```
GET /
```

---

## Statistics

```
GET /stats
```

---

## Ask Database

```
POST /ask
```

Example

```json
{
    "question":"Show all Female users"
}
```

---

# 🖥 Sample Query

### Input

```
Show all Female users
```

### Generated SQL

```sql
SELECT *
FROM users
WHERE gender='Female';
```

### Result

Returns all female users.

---

# 🎯 Screenshots

## Home Page

<img width="1890" height="906" alt="Screenshot 2026-07-18 221050" src="https://github.com/user-attachments/assets/e65cbd26-d347-4710-a3fc-e530040a7490" />


---

## Generated SQL

<img width="1042" height="493" alt="Screenshot 2026-07-19 115509" src="https://github.com/user-attachments/assets/c89fdf2b-ee28-46cf-a165-096bdb7a04df" />

---

## Query Result

<img width="683" height="831" alt="Screenshot 2026-07-19 115542" src="https://github.com/user-attachments/assets/0fcf8a25-3c19-48e0-bf15-d602181fbba5" />

---

## AI Explanation

<img width="657" height="197" alt="Screenshot 2026-07-19 115605" src="https://github.com/user-attachments/assets/c517df32-e866-4566-9b57-7d80686aa3af" />


---

## Swagger API

<img width="1890" height="890" alt="Screenshot 2026-07-18 220804" src="https://github.com/user-attachments/assets/0aed14a4-e8a0-4d9b-913f-26f09c1ff541" />

<img width="1902" height="880" alt="Screenshot 2026-07-18 220816" src="https://github.com/user-attachments/assets/a2b0f0e6-727c-4cd0-9072-892eaa6dad3c" />

<img width="1882" height="632" alt="Screenshot 2026-07-18 220824" src="https://github.com/user-attachments/assets/69c3cf8f-2ea9-4dde-b476-f00dcd94737c" />


---

# 🚀 Deployment

## Backend

Render

https://text2sql-a5mj.onrender.com

---

## Frontend

Vercel

https://text2sql-ruby.vercel.app/

---

# 📈 Future Enhancements

- User Authentication
- Query History
- Saved Queries
- Database Upload
- Multiple Database Support
- Query Visualization
- Charts and Graphs
- Role-Based Access
- AI Chat Memory
- Voice-to-SQL
- Multi-language Support

---

# 👩‍💻 Author

**Deepa R**

B.E Computer Science and Engineering (Artificial Intelligence & Machine Learning)

Sri Sai Ram Engineering College

GitHub

https://github.com/Deepa-R-16

---

# 🙏 Acknowledgements

- Google Gemini AI
- FastAPI
- React
- PostgreSQL
- Render
- Vercel

---

# ⭐ If you found this project useful, please give it a star on GitHub.
