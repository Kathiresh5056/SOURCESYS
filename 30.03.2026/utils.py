import pandas as pd

def load_data(file_path):
    return pd.read_csv(file_path)

def get_sample(df):
    return df.head(5).to_dict(orient='records')

def get_basic_info(df):
    return {
        "shape": df.shape,
        "columns": list(df.columns),
        "missing_values": df.isnull().sum().to_dict(),
        "dtypes": df.dtypes.astype(str).to_dict()
    }