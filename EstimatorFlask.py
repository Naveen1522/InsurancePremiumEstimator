from flask import Flask, request, jsonify
import pickle
import numpy as np
from flask_cors import CORS

# Initialize the Flask app
app = Flask(__name__)
CORS(app)  # Enable CORS for public access

# Load the model and scaler
model = pickle.load(open("models/premium_model.pkl", "rb"))
scaler = pickle.load(open("models/scaler.pkl", "rb"))

# Root route
@app.route('/')
def home():
    return "Welcome to the Insurance Premium Estimator API! Use POST /predict to get predictions."

# Define the prediction endpoint
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Get input JSON
        data = request.get_json()

        # Extract the required fields in order
        features = [
            data['Age'],
            data['BMI'],
            data['NumberOfMajorSurgeries'],
            data['Diabetes'],
            data['BloodPressureProblems'],
            data['AnyTransplants'],
            data['AnyChronicDiseases'],
            data['KnownAllergies'],
            data['HistoryOfCancerInFamily']
        ]

        # Convert to array and scale
        features_array = np.array([features])
        scaled_features = scaler.transform(features_array)

        # Predict premium
        prediction = model.predict(scaled_features)[0]

        return jsonify({"estimated_premium": round(prediction, 2)})
    
    except Exception as e:
        return jsonify({"error": str(e)})

# Run the app
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
