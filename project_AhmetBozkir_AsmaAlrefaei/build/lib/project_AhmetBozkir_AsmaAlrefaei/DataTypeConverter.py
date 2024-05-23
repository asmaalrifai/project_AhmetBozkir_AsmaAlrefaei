import pandas as pd
import numpy as np

def to_numeric(df):
    text_columns = df.select_dtypes(include=[object]).columns
    for column in text_columns:
        df[column] = pd.to_numeric(df[column], errors='coerce')

def to_categorical(df):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        df[column] = df[column].astype('category')
