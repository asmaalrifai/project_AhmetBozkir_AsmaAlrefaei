def write_to_file_xls(df, fileNumber):
    file_path = 'c:\\data' + fileNumber + '.xlsx'
    df.to_excel(file_path, index=False)
    print("Data has been written to", file_path, "as xls")

def write_to_file_csv(df, fileNumber):
    file_path = 'c:\\data' + fileNumber + '.csv'
    df.to_csv(file_path, index=False)
    print("Data has been written to", file_path, "as csv")
