import sqlite3

import pandas as pd
from settings import DB_PATH


def save_crypto_data(crypto_data_df: pd.DataFrame):
    """Saves the crypto and crypto_data DataFrames into their respective tables in the database.

    Args:
        crypto_data_df (DataFrame): formatted crypto time series data dataframe.
    """
    with sqlite3.connect(DB_PATH) as conn:
        # NOTE: save crypto_data df to crypto_data table
        crypto_data_df.to_sql("crypto_data", conn, if_exists="append", index=False)
