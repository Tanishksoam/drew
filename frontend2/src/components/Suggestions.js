import React from "react";

const Suggestions = ({ suggestions }) => {
  return (
    <div className="suggestions">
      {suggestions.map((suggestion, index) => (
        <img key={index} src={suggestion} alt={`suggestion-${index}`} />
      ))}
    </div>
  );
};

export default Suggestions;
