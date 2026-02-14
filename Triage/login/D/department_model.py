import pandas as pd
import joblib

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

department_model = joblib.load(os.path.join(BASE_DIR, "department_model.pkl"))
department_features = joblib.load(os.path.join(BASE_DIR, "department_model_features.pkl"))

def predict_department(input_row):

    # Convert input to DataFrame
    if isinstance(input_row, dict):
        df = pd.DataFrame([input_row])
    elif isinstance(input_row, pd.Series):
        df = pd.DataFrame([input_row.to_dict()])
    elif isinstance(input_row, pd.DataFrame):
        df = input_row.copy()
    else:
        raise ValueError("Input must be dict, Series, or DataFrame")

    # Remove label column if present
    if "Department" in df.columns:
        df = df.drop(columns=["Department"])

    # Apply same encoding used during training
    df = pd.get_dummies(df, columns=["Gender"], drop_first=True)
    df = pd.get_dummies(df, columns=["Risk"], drop_first=True)

    # Add missing columns
    for col in department_features:
        if col not in df.columns:
            df[col] = 0

    # Keep only trained columns in correct order
    df = df[department_features]

    # Predict
    prediction = department_model.predict(df)[0]
    probabilities = department_model.predict_proba(df)[0]

    class_index = list(department_model.classes_).index(prediction)
    confidence = round(probabilities[class_index] * 100, 2)

    return {
        "Department": prediction,
        "Confidence": confidence
    }
