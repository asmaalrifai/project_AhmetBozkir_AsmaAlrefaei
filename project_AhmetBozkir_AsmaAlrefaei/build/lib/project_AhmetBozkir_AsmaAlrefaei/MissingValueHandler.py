import numpy as np

def impute_mean(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].mean())

def impute_median(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        df[column] = df[column].fillna(df[column].median())

def impute_constant(df, constant):
    columns = df.columns
    for column in columns:
        df[column] = df[column].fillna(constant)

def delete_missing(df):
    return df.dropna()
