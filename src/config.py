RAW_DATA_PATH = "data/raw/telco_customer_churn.csv"
PROCESSED_DATA_PATH = "data/processed/cleaned_churn.csv"
MODEL_PATH = "model/churn_pipeline.pkl"

TARGET_COLUMN = "Churn Value"

NUM_FEATURES = [
    "Tenure Months",
    "Monthly Charges",
    "Total Charges"
]

CAT_FEATURES = [
    "Contract",
    "Internet Service",
    "Payment Method",
    "Senior Citizen"
]