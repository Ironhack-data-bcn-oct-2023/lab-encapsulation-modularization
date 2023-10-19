import pandas as pd
def basic_cleaning(df, cleaned_file_name):
    """
    Perform basic data cleaning on a DataFrame and export the cleaned data to a CSV file.

    This function removes duplicates, handles missing values, and renames columns.

    Parameters:
        df (pd.DataFrame): The input DataFrame to be cleaned.
        output_path (str): The file path where the cleaned DataFrame should be exported as a CSV file.

    Returns:
        Cleaned dataframe

    Example:
        basic_cleaning(my_dataframe, 'cleaned_data.csv')
    """
    df.dropna(how="any", inplace=True)

    df.columns = [i.lower().replace(" ", "_") for i in df.columns]

    df.to_csv(f"data/{cleaned_file_name}", index=False)

    return df