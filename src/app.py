from flask import Flask, render_template, request
import joblib
import numpy as np
import pickle

app = Flask(__name__)

# Load the trained model and label encoder
model = joblib.load("models/crop_model.pkl")
with open("models/label_encoder.pkl", "rb") as f:
    label_encoder = pickle.load(f)

@app.route('/')
def home():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        features = [
            float(request.form['N']),
            float(request.form['P']),
            float(request.form['K']),
            float(request.form['temperature']),
            float(request.form['humidity']),
            float(request.form['ph']),
            float(request.form['rainfall'])
        ]
        final_features = np.array([features])

        # Predict probabilities
        probabilities = model.predict_proba(final_features)[0]

        # Get top 3 crops
        top_indices = probabilities.argsort()[-3:][::-1]
        top_crops = [(label_encoder.classes_[i], round(probabilities[i] * 100, 2)) for i in top_indices]

        # Format predictions for display
        formatted_predictions = [f"{crop} ({prob}%)" for crop, prob in top_crops]

        return render_template("result.html", prediction=formatted_predictions)

if __name__ == "__main__":
    app.run(debug=True)
