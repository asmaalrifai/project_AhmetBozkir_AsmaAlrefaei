import pandas as pd
import numpy as np

def to_datetime(df):
    text_columns = df.select_dtypes(include=[object]).columns
    for column in text_columns:
        df[column] = pd.to_datetime(df[column], format='%d/%m/%Y', errors='coerce')

def extract_date_part(df, part):
    datetime_columns = df.select_dtypes(include=[np.datetime64]).columns
    for column in datetime_columns:
        if part == 'year':
            df[f'{column}_year'] = df[column].dt.year
        elif part == 'month':
            df[f'{column}_month'] = df[column].dt.month
        elif part == 'day':
            df[f'{column}_day'] = df[column].dt.day
        elif part == 'hour':
            df[f'{column}_hour'] = df[column].dt.hour
        elif part == 'minute':
            df[f'{column}_minute'] = df[column].dt.minute
        elif part == 'second':
            df[f'{column}_second'] = df[column].dt.second
