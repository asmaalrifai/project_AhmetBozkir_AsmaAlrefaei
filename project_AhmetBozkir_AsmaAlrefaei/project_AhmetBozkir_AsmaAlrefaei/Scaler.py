import numpy as np
from sklearn.preprocessing import StandardScaler, MinMaxScaler

def standardize(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        scaler = StandardScaler()
        df[column] = scaler.fit_transform(df[[column]])

def normalize(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        scaler = MinMaxScaler()
        df[column] = scaler.fit_transform(df[[column]])
