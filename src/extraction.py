import os
import pandas as pd
def downloading (url, name):
    """
    Download a file from a given URL and save it with a specified name in the 'data' directory.
    Create a pandas dataframe with the downloaded file and return it

    Parameters:
        url (str): The URL of the file to be downloaded.
        name (str): The name to be used for the downloaded file.

    Returns:
        int: The return code of the shell command executed for downloading (0 for success, non-zero for failure).

    Example:
        return_code = downloading('https://example.com/datafile.csv', 'downloaded_data.csv')
    """
    os.system(f"curl {url} > data/{name}")
    return pd.read_csv(f"data/{name}")