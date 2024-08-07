import React, { useRef, useState } from "react";
import "./Canvas.css";
import { sendSketch } from "../utils/api";

const Canvas = ({ onSketchComplete }) => {
  const canvasRef = useRef(null);
  const [drawing, setDrawing] = useState(false);

  const startDrawing = ({ nativeEvent }) => {
    const { offsetX, offsetY } = nativeEvent;
    const context = canvasRef.current.getContext("2d");
    context.beginPath();
    context.moveTo(offsetX, offsetY);
    setDrawing(true);
  };

  const draw = ({ nativeEvent }) => {
    if (!drawing) return;
    const { offsetX, offsetY } = nativeEvent;
    const context = canvasRef.current.getContext("2d");
    context.lineTo(offsetX, offsetY);
    context.stroke();
  };

  const endDrawing = async () => {
    const context = canvasRef.current.getContext("2d");
    setDrawing(false);
    context.closePath();

    const sketch = canvasRef.current.toDataURL();
    const response = await sendSketch(sketch);
    onSketchComplete(response);
  };

  return (
    <canvas
      ref={canvasRef}
      onMouseDown={startDrawing}
      onMouseMove={draw}
      onMouseUp={endDrawing}
      className="canvas"
    />
  );
};

export default Canvas;
