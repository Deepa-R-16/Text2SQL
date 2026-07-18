import { FaSearch } from "react-icons/fa";

function SearchBox({
    question,
    setQuestion,
    askAI,
    runExample,
    loading
}) {

    return (

        <>

            <div className="aiBox">

                <h2>💬 Ask your database anything</h2>

                <p>Try examples:</p>

                <div className="examples">

                    <button
                        onClick={() =>
                            runExample("Show all female users")
                        }
                    >
                        Show all female users
                    </button>

                    <button
                        onClick={() =>
                            runExample("Show all products")
                        }
                    >
                        Show all products
                    </button>

                    <button
                        onClick={() =>
                            runExample("Show total number of orders")
                        }
                    >
                        Total orders
                    </button>

                </div>

                <input
                    type="text"
                    value={question}
                    onChange={(e) =>
                        setQuestion(e.target.value)
                    }
                    onKeyDown={(e) => {
                        if (e.key === "Enter")
                            askAI();
                    }}
                    placeholder="Ask your database question..."
                    className="inputBox"
                />

            </div>

            <br />
            <br />

            <button
                onClick={askAI}
                disabled={loading}
                className="button"
            >
                <FaSearch style={{ marginRight: "8px" }} />

                {loading ? "Thinking..." : "Ask AI"}

            </button>

        </>

    );

}

export default SearchBox;