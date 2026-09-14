from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os

# Initialize Flask app
app = Flask(__name__)

# Load the saved pipeline from model folder
model_path = os.path.join("model", "fuel_pipeline.joblib")
pipeline = joblib.load(model_path)

# Home route: render HTML form
@app.route('/')
def home():
    return render_template('index.html')

# Predict route: handles form input or JSON API
@app.route('/predict', methods=['POST'])
def predict():
    try:
        # If data comes from form
        if request.form:
            feature1 = float(request.form['feature1'])
            feature2 = float(request.form['feature2'])
            feature3 = float(request.form['feature3'])
            feature4 = float(request.form['feature4'])
            feature5 = float(request.form['feature5'])
        # If data comes from JSON API
        elif request.json:
            data = request.get_json()
            feature1 = float(data['feature1'])
            feature2 = float(data['feature2'])
            feature3 = float(data['feature3'])
            feature4 = float(data['feature4'])
            feature5 = float(data['feature5'])
        else:
            return jsonify({"error": "No input provided"}), 400

        # Prepare features for prediction
        features = np.array([[feature1, feature2, feature3, feature4, feature5]])
        prediction = pipeline.predict(features)

        # Return prediction in HTML page
        return render_template('index.html', prediction_text=f"Predicted Fuel Efficiency: {prediction[0]:.2f}")
    
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)
