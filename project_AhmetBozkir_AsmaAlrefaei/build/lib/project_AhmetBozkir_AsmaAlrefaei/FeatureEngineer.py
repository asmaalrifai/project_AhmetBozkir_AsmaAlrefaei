def create_interaction_feature(df, column1, column2, new_column_name):
    if column1 not in df.columns or column2 not in df.columns:
        raise KeyError(f"One or both columns: '{column1}', '{column2}' are not in the DataFrame.")
    df[new_column_name] = df[column1] * df[column2]

def create_polynomial_feature(df, column, degree, new_column_name):
    if column not in df.columns:
        raise KeyError(f"Column '{column}' is not in the DataFrame.")
    df[new_column_name] = df[column] ** degree
