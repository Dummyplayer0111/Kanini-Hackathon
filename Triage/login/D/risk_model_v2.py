import pandas as pd
import joblib

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

risk_model = joblib.load(os.path.join(BASE_DIR, "triage_model.pkl"))
risk_features = joblib.load(os.path.join(BASE_DIR, "model_features.pkl"))

def predict_risk_dummy(input_row, top_n=8, threshold=10):
    print(input_row)

def predict_risk(input_row, top_n=8, threshold=10):

    # Convert input to DataFrame
    if isinstance(input_row, dict):
        df = pd.DataFrame([input_row])
    elif isinstance(input_row, pd.Series):
        df = pd.DataFrame([input_row.to_dict()])
    elif isinstance(input_row, pd.DataFrame):
        df = input_row.copy()
    else:
        raise ValueError("Input must be dict, Series, or DataFrame")

    # Remove label columns if present
    for col in ["Risk", "Department"]:
        if col in df.columns:
            df = df.drop(columns=[col])

    # Encode Gender (same as training)
    df = pd.get_dummies(df, columns=["Gender"], drop_first=True)

    # Add missing columns
    for col in risk_features:
        if col not in df.columns:
            df[col] = 0

    # Keep only trained columns
    df = df[risk_features]

    # Predict
    prediction = risk_model.predict(df)[0]
    probabilities = risk_model.predict_proba(df)[0]

    class_index = list(risk_model.classes_).index(prediction)
    confidence = round(probabilities[class_index] * 100, 2)

    # Compute contribution scores
    importances = risk_model.feature_importances_
# Ensure numeric before multiplication
    numeric_row = df.iloc[0].astype(float)
    contribution_scores = numeric_row * importances


    contribution_df = pd.DataFrame({
        "Feature": risk_features,
        "Contribution": contribution_scores
    })

    contribution_df = contribution_df.sort_values(
        by="Contribution",
        ascending=False
    )
    
    contribution_df = contribution_df[
        contribution_df["Contribution"] > threshold
    ]


    top_factors = contribution_df.head(top_n)

    return {
        "Risk": prediction,
        "Confidence": confidence,
        "Top_Contributing_Factors": top_factors.to_dict()
    }
