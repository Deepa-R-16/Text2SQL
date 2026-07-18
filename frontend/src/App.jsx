import SearchBox from "./components/SearchBox";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { tomorrow } from "react-syntax-highlighter/dist/esm/styles/prism";
import Header from "./components/Header";

import * as XLSX from "xlsx";
import { useState, useEffect } from "react";
import axios from "axios";
import "./App.css";

function App() {
  const [darkMode, setDarkMode] = useState(false);
  const [question, setQuestion] = useState("");
  const [response, setResponse] = useState(null);
  const [loading, setLoading] = useState(false);
  const [history, setHistory] = useState([]);
  const [stats, setStats] = useState(null);

  useEffect(() => {
  axios
    .get("http://127.0.0.1:8000/stats")
    .then((res) => {
      setStats(res.data);
    })
    .catch((err) => {
      console.log(err);
    });
}, []);

  async function askAI() {
    if (question.trim() === "") return;

    setLoading(true);

    try {
      const res = await axios.post("http://127.0.0.1:8000/ask", {
  question: question,
});

setResponse(res.data);

setHistory([
  ...history,
  {
    question: question,
    sql: res.data.generated_sql,
    answer: res.data.ai_answer
  }
]);

setQuestion("");
    } catch (error) {
  console.error(error);

  alert(
    error.response?.data?.detail ||
    error.response?.data?.ai_answer ||
    error.message ||
    "Backend Connection Failed"
  );
}

    setLoading(false);
  }

  async function runExample(exampleQuestion){

  setQuestion(exampleQuestion);

  setLoading(true);

  try {

    const res = await axios.post(
      "http://127.0.0.1:8000/ask",
      {
        question: exampleQuestion
      }
    );


    setResponse(res.data);


    setHistory([
      ...history,
      {
        question: exampleQuestion,
        sql: res.data.generated_sql,
        answer: res.data.ai_answer
      }
    ]);


  } 
  catch(error){

    console.log(error);

    alert("Query failed");

  }


  setLoading(false);

}

  function downloadJSON() {

  const data = JSON.stringify(response.result, null, 2);

  const blob = new Blob([data], {
    type: "application/json",
  });

  const url = window.URL.createObjectURL(blob);

  const a = document.createElement("a");

  a.href = url;

  a.download = "query_result.json";

  a.click();

  window.URL.revokeObjectURL(url);
}

function downloadCSV() {

  const headers = Object.keys(response.result[0]).join(",");

  const rows = response.result.map((row) =>
    Object.values(row).join(",")
  );

  const csv = [headers, ...rows].join("\n");

  const blob = new Blob([csv], {
    type: "text/csv",
  });

  const url = window.URL.createObjectURL(blob);

  const a = document.createElement("a");

  a.href = url;

  a.download = "query_result.csv";

  a.click();

  window.URL.revokeObjectURL(url);
}

function downloadExcel() {
  const worksheet = XLSX.utils.json_to_sheet(response.result);

  const workbook = XLSX.utils.book_new();

  XLSX.utils.book_append_sheet(
    workbook,
    worksheet,
    "Results"
  );

  XLSX.writeFile(workbook, "query_result.xlsx");
}
async function copySQL() {

await navigator.clipboard.writeText(
  response.generated_sql
);

alert("SQL copied successfully!");

}

  return (
<div className={darkMode ? "dark" : ""}>

<div className="container">      <Header
  darkMode={darkMode}
  setDarkMode={setDarkMode}
/>
      <div className="hero">

<h2>
Ask Anything About Your Database
</h2>

<p>
Transform natural language questions into SQL queries
using Gemini AI and retrieve intelligent database insights.
</p>

</div>





      
      {stats && (
  <div className="dashboard">

    <h2>Database Overview</h2>

    <div className="statsContainer">

      <div className="statCard">
        <h3>👤 Users</h3>
        <p>{stats.users}</p>
      </div>


      <div className="statCard">
        <h3>🛒 Products</h3>
        <p>{stats.products}</p>
      </div>


      <div className="statCard">
        <h3>📦 Orders</h3>
        <p>{stats.orders}</p>
      </div>

    </div>

  </div>
)}

      <hr />

      <SearchBox
  question={question}
  setQuestion={setQuestion}
  askAI={askAI}
  runExample={runExample}
  loading={loading}
/>

      <br />
      <br />

      {loading && (
  <div className="loading">
    🤖 Gemini is Thinking...
  </div>
)}
      {history.length > 0 && (
<div className="card">

<h2>Conversation History</h2>

<button
onClick={() => setHistory([])}
style={{marginBottom:"15px"}}
>
🗑 Clear History
</button>


{history.map((item,index)=>(

<div key={index} className="historyItem">

<h4>
👤 Question {index+1}
</h4>

<p>
{item.question}
</p>

<hr/>

</div>

))}

</div>
)}

      {response && (
        <>
          <hr />

          {/* Generated SQL */}

          <div className="card">
            <h2>Generated SQL</h2>

            <SyntaxHighlighter
  language="sql"
  style={tomorrow}
  customStyle={{
    borderRadius:"12px",
    padding:"20px",
    fontSize:"15px"
  }}
>
{response.generated_sql}
</SyntaxHighlighter>

<button
  onClick={copySQL}
  style={{ marginTop: "10px" }}
>
  📋 Copy SQL
</button>
          </div>

          {/* Query Result */}

          <div className="card">
            <h2>Query Result</h2>
            <div className="resultInfo">

<div className="infoCard">
⏱ {response.execution_time} sec
</div>


<div className="infoCard">
📊 {response.rows} Rows
</div>


<div className="infoCard">
📁 {response.result.length} Records
</div>

</div>
            
            <div style={{ marginBottom: "15px" }}>

  <button onClick={downloadCSV}>
    📄 Download CSV
  </button>

  <button
    onClick={downloadExcel}
    style={{ marginLeft: "10px" }}
  >
    📊 Download Excel
  </button>

  <button
    onClick={downloadJSON}
    style={{ marginLeft: "10px" }}
  >
    📝 Download JSON
  </button>
  <p style={{ marginBottom: "10px", fontWeight: "bold" }}>
  Total Records: {response.result.length}
</p>

</div>

            <table className="resultTable">
              <thead>
                <tr>
                  {response.result.length > 0 &&
                    Object.keys(response.result[0]).map((key) => (
                      <th key={key}>{key}</th>
                    ))}
                </tr>
              </thead>

              <tbody>
                {response.result.slice(0, 20).map((row, index) => (
                  <tr key={index}>
                    {Object.values(row).map((value, i) => (
                      <td key={i}>{String(value)}</td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>

            {response.result.length > 20 && (
              <p style={{ marginTop: "15px", color: "gray" }}>
                Showing first 20 rows of {response.result.length} total rows.
              </p>
            )}
          </div>

          {/* AI Answer */}

          <div className="card">
            <h2>AI Answer</h2>

            <div className="answerBox">
              {response.ai_answer}
            </div>
          </div>
        </>
      )}

      <hr />

<p className="footer">
  AI Text-to-SQL Assistant | Developed using React, FastAPI, PostgreSQL & Gemini AI
</p>

</div>

</div>
  );
}

export default App;