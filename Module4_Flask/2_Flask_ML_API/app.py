from flask import Flask
from flask import request, jsonify, make_response
import pickle
import numpy as np
from sklearn.datasets import load_iris


iris_types = load_iris().target_names

app = Flask(__name__)

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get data from request
        data = request.get_json()

        # Validate input
        if 'features' not in data:
            return jsonify({"error": "Missing 'features' key in the input data"}), 400

        features = data['features']

        # Check if it's a single prediction or multiple
        if isinstance(features[0], (int, float)):  # Single prediction
            features = np.array(features).reshape(1, -1)  # Reshape to 2D array
        elif isinstance(features, list):  # Multiple predictions
            features = np.array(features)
        else:
            return jsonify({"error": "Invalid input format"}), 400

        # Make a prediction
        predictions = model.predict(features).tolist()

        # Map predictions to class names
        class_names = load_iris().target_names
        predictions_named = ['Iris-' + class_names[pred] for pred in predictions]

        # Return the prediction as a JSON response
        return make_response(jsonify({'prediction': predictions_named}), 200)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(debug=True)
