from flask import Flask, request, jsonify
import joblib
import numpy as np
import os

app = Flask(__name__)

# Load the model
model_path = 'logistic_regression_model.pkl'
if os.path.exists(model_path):
    logistic_model = joblib.load(model_path)
else:
    raise FileNotFoundError(f"Model file {model_path} not found.")

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    features = np.array(data['features']).reshape(1, -1)

    logistic_prediction = logistic_model.predict(features)

    return jsonify({
        'logistic_regression_prediction': int(logistic_prediction[0])
    })

if __name__ == '__main__':
    from waitress import serve
    print("Starting server...")
    serve(app, host='0.0.0.0', port=5000)
