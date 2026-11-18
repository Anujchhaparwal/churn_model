# Customer Churn Prediction System 🚀

An end-to-end **Machine Learning application** that predicts whether a telecom customer is likely to churn. The system includes data preprocessing, model training, evaluation, a FastAPI-based backend API, a modern Streamlit frontend, Docker containerization, and basic cloud deployment using Render.

---

## 📌 Project Overview

Customer churn is a critical business problem for telecom companies. This project uses customer profile data such as tenure, monthly charges, contract type, and service preferences to predict churn behavior.

The trained model achieves **~79.5% accuracy** and is accessible through:

* A REST API (FastAPI)
* An interactive web interface (Streamlit)
* A Dockerized cloud deployment (Render)

---

## 📂 Project Structure

```
ml-churn-deployment/
│
├── data/
│   ├── raw/                 # Original dataset
│   └── processed/          # Cleaned dataset
│
├── model/
│   └── churn_pipeline.pkl  # Trained ML pipeline
│
├── src/
│   ├── config.py           # Paths & feature configuration
│   ├── data_loader.py      # Data cleaning logic
│   ├── preprocessing.py   # Feature preprocessing
│   ├── train.py            # Model training
│   ├── evaluate.py         # Model evaluation
│   └── visuals.py          # EDA & feature importance
│
├── app/
│   ├── __init__.py
│   └── main.py             # FastAPI backend
│
├── frontend/
│   └── streamlit_app.py    # Streamlit UI
│
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🧠 Machine Learning Pipeline

### 1. Data Cleaning

* Converted **Total Charges** to numeric values
* Filled missing values using `fillna()`

### 2. Preprocessing

* **StandardScaler** for numerical features
* **OneHotEncoder** for categorical features

### 3. Model Training

* Algorithm: **Logistic Regression**
* Implemented using Scikit-learn Pipeline

### 4. Model Evaluation

* Accuracy: **79.49%**
* Balanced performance on non-churn and churn customers

---

## 📊 Model Performance

### Confusion Matrix

```
[[4654  520]
 [ 900  969]]
```

### Classification Report Summary

| Class         | Precision | Recall | F1-score |
| ------------- | --------- | ------ | -------- |
| Non-Churn (0) | 0.84      | 0.90   | 0.87     |
| Churn (1)     | 0.65      | 0.52   | 0.58     |

---

## 🔍 Business Insights

Key factors influencing customer churn:

* High monthly charges
* Month-to-month contracts
* Low tenure (new customers)
* Fiber optic internet users
* Electronic check payment method

These insights are visualized using:

* Churn vs Contract graph
* Churn vs Monthly Charges chart
* Feature Importance plot

---

## 🔗 API Endpoints (FastAPI)

### Health Check

```
GET /health
```

### Churn Prediction

```
POST /predict
```

Sample Request:

```json
{
  "Tenure_Months": 12,
  "Monthly_Charges": 70.5,
  "Total_Charges": 850,
  "Contract": "Month-to-month",
  "Internet_Service": "Fiber optic",
  "Payment_Method": "Electronic check",
  "Senior_Citizen": "No"
}
```

Sample Response:

```json
{
  "churn_prediction": 1,
  "churn_probability": 0.78,
  "message": "Customer is likely to churn"
}
```

---

## 🎨 Frontend (Streamlit)

The Streamlit UI allows users to:

* Enter customer details
* Get churn predictions
* View risk levels (High / Medium / Low)
* Receive randomized retention recommendations

### Risk Levels

| Probability | Risk Level |
| ----------- | ---------- |
| > 0.7       | 🔴 High    |
| 0.4 – 0.7   | 🟡 Medium  |
| < 0.4       | 🟢 Low     |

---

## ▶️ Run Locally (Without Docker)

1. Activate virtual environment
2. Install dependencies from `requirements.txt`
3. Start FastAPI backend
4. Launch Streamlit frontend

The API can be accessed at:

```
http://127.0.0.1:8000/docs
```

The frontend runs at:

```
http://localhost:8501
```

---

## 🐳 Docker Setup (Local)

The backend is containerized using Docker for consistent deployment.

Steps:

* Build the Docker image
* Run the container on port 10000
* Access the API using `/health` or `/docs`

---

## ☁️ Cloud Deployment (Render – Overview)

The application is deployed using **Render** with Docker support.

Basic process:

* Connect the GitHub repository to Render
* Select Docker as the runtime
* Deploy the application

Render provides a public URL to access the API endpoints online.

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
| Streamlit    | Frontend UI         |
| Matplotlib   | Data visualization  |
| Docker       | Containerization    |
| Render       | Cloud deployment    |

---

## 🚀 Future Enhancements

* Business analytics dashboard
* PDF churn reports
* Admin monitoring panel
* Model retraining pipeline
* User authentication

---

## 👨‍💻 Author

**Anuj Chhaparwal**
Machine Learning & Backend Developer

---

## 📜 License

This project is for educational and demonstration purposes only.
