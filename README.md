# AI-Health-Predictor
# 🩺 AI Disease Prediction System

## Overview

AI Disease Prediction System is a Machine Learning-based healthcare application that predicts possible diseases based on user-selected symptoms.

The application uses a **Random Forest Classifier** to analyze symptoms and provide disease predictions with confidence scores and precautions.

---

## Features

- 🔍 Symptom-based disease prediction
- 📊 Confidence score for predictions
- 📈 Model performance dashboard
- 📖 Disease information and precautions
- 🎨 Interactive Streamlit user interface

---

## Machine Learning Model

**Algorithm:** Random Forest Classifier

**Type:** Supervised Machine Learning

**Input:** Patient symptoms

**Output:** Predicted disease

---

## Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Joblib

---

## Project Structure

AI-Disease-Prediction-System/

│── Home.py
│── medical_model.pkl
│── Training.csv
│── disease_info.csv
│── requirements.txt

└── pages/
├── Prediction.py
├── Model_Performance.py
└── About_Project.py


## Installation

### Clone the repository

```bash
git clone https://github.com/yourusername/AI-Disease-Prediction-System.git

Navigate to project folder
```bash
cd AI-Disease-Prediction-System

Install dependencies
```bash
pip install -r requirements.txt

Run the application
```bash
streamlit run app.py


