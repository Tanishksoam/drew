export const sendSketch = async (sketch) => {
  const response = await fetch("http://localhost:5000/recognize", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ sketch }),
  });
  return response.json();
};
