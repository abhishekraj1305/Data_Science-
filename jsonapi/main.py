from flask import Flask, request, jsonify

app = Flask(__name__)

# @app.route('/api/predict', methods=['GET'])
# def predict():
#     value = request.args.get('value')
    
#     if value is None:
#         return jsonify({'error': 'Missing input'}), 400

#     # Simulated prediction (replace with actual model call)
#     result = int(value) * 2

#     return jsonify({
#         'input': value,
#         'prediction': result
#     })
    
    
@app.route("/")

def hello_world():
    data = {"output":45, "Accuracy":98.98}
    return jsonify(data),200

app.run(debug=True)