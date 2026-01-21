from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

from src.config import MODEL_PATH,CAT_FEATURES,NUM_FEATURES

app=FastAPI(title="Customer Churn Prediction API")

model=joblib.load(MODEL_PATH)

class CustomerData(BaseModel):
    Tenure_Months:int
    Monthly_Charges:float
    Total_Charges:float
    Contract:str
    Internet_Service:str
    Payment_Method:str
    Senior_Citizen:str

@app.get("/health")
def health():
        return {"status":"ok"}
    
@app.post("/predict")
def predict(data: CustomerData):
    input_dict={
        "Tenure Months":data.Tenure_Months,
        "Monthly Charges":data.Monthly_Charges,
        "Total Charges":data.Total_Charges,
        "Contract":data.Contract,
        "Internet Service":data.Internet_Service,
        "Payment Method":data.Payment_Method,
        "Senior Citizen":data.Senior_Citizen
    }

    df=pd.DataFrame([input_dict])
    prediction = model.predict(df)[0]
    probability = model.predict_proba(df)[0][1]


    return {
        "Churn_Prediction": int(prediction),
        "Churn_Probability": float(probability),
        "message": "Customer is likely to churn" if prediction == 1 else "Customer is likely to Stay"
    }