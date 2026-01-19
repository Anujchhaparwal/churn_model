import pandas as pd
from config import RAW_DATA_PATH, PROCESSED_DATA_PATH

def load_raw_data():
    df = pd.read_csv(RAW_DATA_PATH)
    return df

def data_cleaning(df):
    df = df.copy()
    df['Total Charges'] = pd.to_numeric(df['Total Charges'],errors = 'coerce')
    df['Total Charges'].fillna(0,inplace = True)
    return df

def save_processed_data(df):
    df.to_csv(PROCESSED_DATA_PATH,index = False)

if __name__ == '__main__':
    df = load_raw_data()
    print("Raw Data Shape",df.shape)
    df_clean = data_cleaning(df)
    print("Cleaned Data Shape",df.shape)
    save_processed_data(df_clean)
    print("Cleaned Data Saved")
