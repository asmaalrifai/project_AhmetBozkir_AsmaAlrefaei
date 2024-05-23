import numpy as np

def remove_outliers_iqr(df, threshold=1.5):
    numeric_columns = df.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        Q1 = df[column].quantile(0.25)
        Q3 = df[column].quantile(0.75)
        IQR = Q3 - Q1
        lower_bound = Q1 - (IQR * threshold)
        upper_bound = Q3 + (IQR * threshold)
        df = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    return df
