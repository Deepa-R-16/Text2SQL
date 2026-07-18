function Header({ darkMode, setDarkMode }) {
  return (
    <header className="header">
      <div>
        <h1>AI Text-to-SQL Assistant</h1>

        <p>
          Convert Natural Language Questions into SQL Queries using Gemini AI
        </p>
      </div>

      <button
        className="theme-btn"
        onClick={() => setDarkMode(!darkMode)}
      >
        {darkMode ? "☀ Light Mode" : "🌙 Dark Mode"}
      </button>
    </header>
  );
}

export default Header;