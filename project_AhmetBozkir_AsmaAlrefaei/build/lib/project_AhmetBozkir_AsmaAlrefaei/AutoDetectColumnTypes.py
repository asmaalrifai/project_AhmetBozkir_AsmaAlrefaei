import numpy as np

def auto_detect_column_types(df):
    column_types = {
        'numeric': df.select_dtypes(include=[np.number]).columns.tolist(),
        'text': df.select_dtypes(include=[object]).columns.tolist(),
        'datetime': df.select_dtypes(include=[np.datetime64]).columns.tolist()
    }
    return column_types
