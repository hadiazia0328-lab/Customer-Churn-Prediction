
from pathlib import Path

import joblib
import pandas as pd

# Project paths
PROJECT_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = PROJECT_DIR / "models" / "churn_model.joblib"

# Load the trained pipeline
model = joblib.load(MODEL_PATH)


def predict_churn(customer_data):
    """
    Predict whether a customer is likely to leave.

    customer_data: dictionary containing customer features.
    """
    customer_df = pd.DataFrame([customer_data])

    prediction = model.predict(customer_df)[0]
    probability = model.predict_proba(customer_df)[0][1]

    result = "Yes" if prediction == 1 else "No"

    return {
        "churn_prediction": result,
        "churn_probability": round(float(probability) * 100, 2),
    }


if __name__ == "__main__":
    sample_customer = {
        "gender": "Female",
        "SeniorCitizen": 0,
        "Partner": "No",
        "Dependents": "No",
        "tenure": 2,
        "PhoneService": "Yes",
        "MultipleLines": "No",
        "InternetService": "Fiber optic",
        "OnlineSecurity": "No",
        "OnlineBackup": "No",
        "DeviceProtection": "No",
        "TechSupport": "No",
        "StreamingTV": "No",
        "StreamingMovies": "No",
        "Contract": "Month-to-month",
        "PaperlessBilling": "Yes",
        "PaymentMethod": "Electronic check",
        "MonthlyCharges": 75.0,
        "TotalCharges": 150.0,
    }

    result = predict_churn(sample_customer)

    print("Churn Prediction:", result["churn_prediction"])
    print("Churn Probability:", f'{result["churn_probability"]}%')
