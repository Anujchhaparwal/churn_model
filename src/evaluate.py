import pandas as pd
import joblib 
from sklearn.metrics import classification_report,confusion_matrix

from config import PROCESSED_DATA_PATH,TARGET_COLUMN,MODEL_PATH,NUM_FEATURES,CAT_FEATURES

def evaluate_model():
    df = pd.read_csv(PROCESSED_DATA_PATH)
    y = df[TARGET_COLUMN]
    x = df[NUM_FEATURES+CAT_FEATURES]

    model=joblib.load(MODEL_PATH)

    y_pred= model.predict(x)

    print("\nClassification Report")
    print(classification_report(y,y_pred))

    print("\nConfusion Matrix")
    print(confusion_matrix(y,y_pred))

if __name__ == "__main__":
    evaluate_model()    
