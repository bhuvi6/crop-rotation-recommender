
---

# 🌱 Crop Rotation Recommender

A **machine learning based web application** that recommends the most suitable crops for sustainable agriculture, based on soil nutrients and environmental conditions.

## 🚀 Features

* Input soil and climate parameters:

  * Nitrogen (N)
  * Phosphorus (P)
  * Potassium (K)
  * Temperature (°C)
  * Humidity (%)
  * pH value
  * Rainfall (mm)
* Predicts **top 3 crops** with probability scores.
* Built with **Flask**, **Scikit-learn**, and **Joblib**.
* Simple, clean web UI for user interaction.

## 🛠️ Tech Stack

* **Backend**: Python, Flask
* **Machine Learning**: Scikit-learn (RandomForestClassifier)
* **Frontend**: HTML, CSS (internal styling)
* **Model Storage**: Joblib, Pickle

## 📂 Project Structure

```
crop-rotation-recommender/
│
├── src/
│   ├── app.py              # Flask app entry point
│   ├── templates/
│   │   ├── index.html      # Input form
│   │   └── result.html     # Prediction result page
│   └── static/             # (optional) CSS/JS/images
│
├── models/
│   ├── crop_model.pkl      # Trained ML model
│   └── label_encoder.pkl   # Label encoder for crops
│
├── dataset.csv             # Training dataset (if included)
├── requirements.txt        # Dependencies
└── README.md               # Project documentation
```

## ⚡ How to Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/bhuvi6/crop-rotation-recommender.git
   cd crop-rotation-recommender
   ```
2. (Optional) Create a virtual environment:

   ```bash
   python -m venv venv
   venv\Scripts\activate   # On Windows
   source venv/bin/activate  # On Mac/Linux
   ```
3. Install dependencies from `requirements.txt`:

   ```bash
   pip install -r requirements.txt
   ```
4. Run the Flask app:

   ```bash
   python src/app.py
   ```
5. Open in browser:

   ```
   http://127.0.0.1:5000
   ```

## 📦 Requirements

All required dependencies are listed in **requirements.txt**:

```
Flask
numpy
pandas
scikit-learn
joblib
```

## 📊 Dataset

The model is trained on a crop recommendation dataset containing soil nutrients, climate parameters, and crop labels.

## 🌍 Future Enhancements

* Add fertilizer recommendations.
* Visualize predictions with charts.
* Deploy on cloud (Heroku/AWS).

---

✨ Built with love for **sustainable farming** 🌱

---


