# churn_model
# Customer Churn Prediction System 🚀

An end-to-end *Machine Learning deployment project* that predicts whether a telecom customer is likely to churn. The system includes data preprocessing, model training, evaluation, and a FastAPI-based backend API.

---

## 📌 Project Overview

Customer churn is a critical business problem for telecom companies. This project uses customer profile data such as tenure, monthly charges, and contract type to predict churn behavior.

The trained model achieves *~79.5% accuracy* and is deployed through a REST API using FastAPI.

---

## 📂 Project Structure


ml-churn-deployment/
│
├── data/
│   ├── raw/              # Original dataset
│   └── processed/       # Cleaned dataset
│
├── model/
│   └── churn_pipeline.pkl   # Trained ML pipeline
│
├── src/
│   ├── config.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── train.py
│   └── evaluate.py
│
├── app/
│   └── main.py           # FastAPI backend
│
├── requirements.txt
├── Dockerfile (coming soon)
└── README.md


---

## 🧠 Machine Learning Pipeline

### 1. Data Cleaning

* Converted *Total Charges* to numeric values
* Filled missing values using fillna()

### 2. Preprocessing

* *StandardScaler* for numerical features
* *OneHotEncoder* for categorical features

### 3. Model Training

* Algorithm: *Logistic Regression*
* Implemented using Scikit-learn Pipeline

### 4. Model Evaluation

* Accuracy: *79.49%*
* Balanced performance on non-churn and churn customers

---

## 🔗 API Endpoints

### Health Check


GET /health


Response:

json
{"status": "ok"}


---

### Churn Prediction


POST /predict


Sample Request:

json
{
  "Tenure_Months": 12,
  "Monthly_Charges": 70.5,
  "Total_Charges": 850,
  "Contract": "Month-to-month",
  "Internet_Service": "Fiber optic",
  "Payment_Method": "Electronic check",
  "Senior_Citizen": "No"
}


Sample Response:

json
{
  "churn_prediction": 1,
  "message": "Customer is likely to churn"
}


---

## ▶️ How to Run Locally

### 1. Activate Virtual Environment


venv\Scripts\activate


### 2. Install Dependencies


pip install -r requirements.txt


### 3. Start the API Server


uvicorn app.main:app --reload


### 4. Open Swagger UI


http://127.0.0.1:8000/docs


---

## 📊 Model Performance

### Confusion Matrix


[[4654  520]
 [ 900  969]]


### Classification Report Summary

| Class         | Precision | Recall | F1-score |
| ------------- | --------- | ------ | -------- |
| Non-Churn (0) | 0.84      | 0.90   | 0.87     |
| Churn (1)     | 0.65      | 0.52   | 0.58     |

---

## 🛠 Tech Stack

| Tool         | Purpose             |
| ------------ | ------------------- |
| Python       | Core language       |
| Pandas       | Data processing     |
| Scikit-learn | ML training         |
| Joblib       | Model serialization |
| FastAPI      | REST API            |
| Pydantic     | Input validation    |
| Uvicorn      | API server          |

---

## 🚀 Next Steps

* Build Streamlit frontend
* Dockerize the app
* Deploy on Render
* Generate public URL
* Record demo video

---

## 👨‍💻 Author

*Anuj Chhaparwal*
Machine Learning & Backend Developer

---

## 📜 License

This project is for educational and demonstration purposes only.
