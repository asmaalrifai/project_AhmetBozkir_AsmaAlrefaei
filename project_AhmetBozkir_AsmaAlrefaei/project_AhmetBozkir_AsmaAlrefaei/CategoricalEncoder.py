import pandas as pd
from sklearn.preprocessing import OneHotEncoder, LabelEncoder

def one_hot_encode(df):
    text_columns = df.select_dtypes(include=[object]).columns
    encoder = OneHotEncoder()
    for column in text_columns:
        encoded = encoder.fit_transform(df[[column]])
        encoded_df = pd.DataFrame(encoded.toarray(), columns=encoder.get_feature_names_out([column]))
        df = df.join(encoded_df)
    return df

def label_encode(df):
    text_columns = df.select_dtypes(include=[object]).columns
    encoder = LabelEncoder()
    for column in text_columns:
        df[column] = encoder.fit_transform(df[column])
