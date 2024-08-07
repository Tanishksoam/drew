import React, { useState } from "react";
import Canvas from "./Canvas";
import Suggestions from "./Suggestions";
import "./App.css";

const App = () => {
  const [suggestions, setSuggestions] = useState([]);

  const handleSketchComplete = (response) => {
    setSuggestions(response.suggestions);
  };

  return (
    <div className="app">
      <Canvas onSketchComplete={handleSketchComplete} />
      <Suggestions suggestions={suggestions} />
    </div>
  );
};

export default App;
