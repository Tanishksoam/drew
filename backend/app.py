from flask import Flask, request, jsonify
from models.sketch_recognition import recognize_sketch
from models.sketch_generation import generate_sketch

app = Flask(__name__)

@app.route('/recognize', methods=['POST'])
def recognize():
    data = request.get_json()
    sketch = data['sketch']
    result = recognize_sketch(sketch)
    return jsonify(result)

@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    sketch = data['sketch']
    result = generate_sketch(sketch)
    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)