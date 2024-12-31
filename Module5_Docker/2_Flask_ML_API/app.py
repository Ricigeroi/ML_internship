import os

from flask import Flask
from flask import request, jsonify, make_response
import pickle
import numpy as np
from sklearn.datasets import load_iris
from flask_sqlalchemy import SQLAlchemy


iris_types = load_iris().target_names

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']

with open('model.pkl', 'rb') as file:
    model = pickle.load(file)

db = SQLAlchemy(app)

class Prediction(db.Model):
    __tablename__ = 'predictions'
    id = db.Column(db.Integer, primary_key=True)
    prediction = db.Column(db.String(20), nullable=False)


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

        for pred in predictions_named:
            new_prediction = Prediction(prediction=pred)

            try:
                db.session.add(new_prediction)
                db.session.commit()
                print('Added new prediction:', new_prediction)
            except Exception as e:
                db.session.rollback()
                return jsonify({"error": str(e)}), 500
        return jsonify({"predictions": predictions_named}), 207
    except Exception as e:
        return jsonify({'error': str(e)}), 400


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
