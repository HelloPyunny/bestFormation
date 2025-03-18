import logo from "./logo.svg";
import "./App.css";

import React, { useState } from "react";

function App() {
  const defaultJson = `{
  "stats": {
    "NAME": {
      "PAC": 60.0,
      "SHO": 65.0,
      "PAS": 71.0,
      "DRI": 76.0,
      "DEF": 67.0,
      "PHY": 74.0,
      "Acceleration": 70.0,
      "Sprint Speed": 62.0,
      "Positioning": 72.0,
      "Finishing": 68.0,
      "Shot Power": 74.0,
      "Long Shots": 72.0,
      "Volleys": 69.0,
      "Penalties": 75.0,
      "Vision": 75.0,
      "Crossing": 70.0,
      "Free Kick Accuracy": 67.0,
      "Short Passing": 76.0,
      "Long Passing": 73.0,
      "Curve": 71.0,
      "Dribbling": 72.0,
      "Agility": 64.0,
      "Balance": 73.0,
      "Reactions": 66.0,
      "Ball Control": 73.0,
      "Composure": 70.0,
      "Interceptions": 65.0,
      "Heading Accuracy": 59.0,
      "Def Awareness": 62.0,
      "Standing Tackle": 68.0,
      "Sliding Tackle": 52.0,
      "Jumping": 59.0,
      "Stamina": 55.0,
      "Strength": 77.0,
      "Aggression": 64.0,
      "Skill moves": 5.0,
      "Weak foot": 1.0,
      "Height": 185.0,
      "GK Diving": 0.0,
      "GK Handling": 0.0,
      "GK Kicking": 0.0,
      "GK Positioning": 0.0,
      "GK Reflexes": 0.0
    }
  }
}`;

  const [inputJson, setInputJson] = useState(defaultJson);
  const [responseData, setResponseData] = useState(null);
  const [errorMsg, setErrorMsg] = useState("");

  // 예측 요청 보내는 함수
  const handlePredict = async () => {
    let parsedData;
    try {
      parsedData = JSON.parse(inputJson);
      setErrorMsg("");
    } catch (error) {
      setErrorMsg("Invalid JSON format.");
      return;
    }

    try {
      const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify(parsedData),
      });
      if (!response.ok) {
        throw new Error("Problem with server request.");
      }
      const result = await response.json();
      setResponseData(result);
    } catch (error) {
      console.error("Prediction Request Error:", error);
      setResponseData({ error: error.message });
    }
  };

  return (
    <div style={{ margin: "20px", fontFamily: "Arial, sans-serif" }}>
      {/* Add logo image */}
      <header style={{ marginBottom: "20px" }}>
        <img src={logo} alt="Logo" style={{ width: "150px" }} />
      </header>

      <h1>Test</h1>
      <p>
        After entering JSON data in the text input box below and clicking the "Predict" button, a
        request is sent to the FastAPI server, and the prediction result is displayed.
      </p>

      <textarea
        style={{ width: "100%", height: "300px", padding: "10px", fontSize: "14px" }}
        value={inputJson}
        onChange={(e) => setInputJson(e.target.value)}
      />

      {errorMsg && <div style={{ color: "red", marginTop: "10px" }}>{errorMsg}</div>}

      <button
        onClick={handlePredict}
        style={{ marginTop: "10px", padding: "10px 20px", fontSize: "16px" }}
      >
        Predict
      </button>

      {responseData && (
        <div style={{ marginTop: "20px" }}>
          <h2>Result</h2>
          <pre>{JSON.stringify(responseData, null, 2)}</pre>
        </div>
      )}
    </div>
  );
}

export default App;
