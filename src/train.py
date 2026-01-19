import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score

from config import PROCESSED_DATA_PATH,TARGET_COLUMN,MODEL_PATH,NUM_FEATURES,CAT_FEATURES
from preprocessing import build_preprocessor
import joblib

def train_model():
    df=pd.read_csv(PROCESSED_DATA_PATH)
    y = df[TARGET_COLUMN]
    x = df[NUM_FEATURES + CAT_FEATURES]

    x_train,x_test,y_train,y_test= train_test_split(x,y,test_size = 0.2,random_state = 42,stratify=y)

    preprocessor=build_preprocessor()

    model = LogisticRegression(max_iter=1000)

    pipeline= Pipeline(steps=[
        ("preprocessor",preprocessor),
        ("classifier",model)

    ])

    pipeline.fit(x_train,y_train)

    y_pred = pipeline.predict(x_test)
    acc= accuracy_score(y_test,y_pred)

    print(f"Model Accuracy:{acc:.2f}")

    joblib.dump(pipeline,MODEL_PATH)
    print("Model saved to: ", MODEL_PATH)

if __name__ == '__main__':
    train_model()



