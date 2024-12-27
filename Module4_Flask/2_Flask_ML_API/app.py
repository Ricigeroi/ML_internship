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
        features = np.array(data['features']).reshape(1, -1)  # Convert to 2D array

        # Make a prediction
        prediction = model.predict(features)[0]

        # Return the prediction as a JSON response
        return make_response(jsonify({'prediction': 'Iris-' + iris_types[int(prediction)]}), 200)
    except Exception as e:
        return jsonify({'error': str(e)})


if __name__ == "__main__":
    app.run(debug=True)
