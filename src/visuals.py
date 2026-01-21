import pandas as pd
import joblib
import matplotlib.pyplot as plt

from config import PROCESSED_DATA_PATH, MODEL_PATH, NUM_FEATURES, CAT_FEATURES

fig_size = (8,5)

def churn_vs_contract():
    df=pd.read_csv(PROCESSED_DATA_PATH)
    churn_contract=pd.crosstab(df["Contract"],df["Churn Value"],normalize="index")

    churn_contract.plot(kind="bar",figsize=fig_size)
    plt.title("Churn Rate by Contract Type")
    plt.ylabel("Proportion")
    plt.tight_layout()
    plt.show()


def churn_vs_monthly_charges():
    df=pd.read_csv(PROCESSED_DATA_PATH)

    plt.figure(figsize=fig_size)
    plt.hist(df[df["Churn Value"]==0]["Monthly Charges"],alpha=0.6,label="No Churn")
    plt.hist(df[df["Churn Value"]==1]["Monthly Charges"],alpha=0.6,label="Churn")
    plt.xlabel("Monthly Charges")
    plt.ylabel("Count")
    plt.title("Churn Rate by Monthly Charges")
    plt.legend()
    plt.tight_layout()
    plt.show()

def feature_importance():
    model=joblib.load(MODEL_PATH)
    classifier= model.named_steps["classifier"]
    
    preprocessor= model.named_steps["preprocessor"]
    feature_names=(
         NUM_FEATURES+list(preprocessor.named_transformers_["cat"].
         get_feature_names_out(CAT_FEATURES)
         )

    )

    importance=classifier.coef_[0]

    imp_df=pd.DataFrame({
        "Feature":feature_names,
        "Importance": importance
    }).sort_values(by="Importance",ascending=False).head(15)


    imp_df.plot(kind="barh",x="Feature",y="Importance",figsize=(10,6))
    plt.title("Top Feature Importance for Churn Prediction")
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    churn_vs_contract()
    churn_vs_monthly_charges()
    feature_importance()
