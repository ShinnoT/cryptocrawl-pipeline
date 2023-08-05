# import sqlite3

# import pandas as pd
# from settings import DB_PATH


# def save_to_db(crypto_df: pd.DataFrame, crypto_data_df: pd.DataFrame):
#     """Saves the crypto and crypto_data DataFrames into their respective tables in the database.

#     Args:
#         crypto_df (DataFrame): formatted crypto metadata dataframe.
#         crypto_data_df (DataFrame): formatted crypto time series data dataframe.
#     """
#     with sqlite3.connect(DB_PATH) as conn:
#         # NOTE: save crypto df to crypto table
#         # TODO: think about whether it's more efficient to replace or fail "if_exists"
#         crypto_df.to_sql("crypto", conn, if_exists="append", index=False)

#         # NOTE: save crypto_data df to crypto_data table
#         crypto_data_df.to_sql("crypto_data", conn, if_exists="append", index=False)
