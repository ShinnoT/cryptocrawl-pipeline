import sqlite3

import pandas as pd
from settings import DB_PATH


def save_crypto(crypto_df: pd.DataFrame):
    """Saves the crypto and crypto_data DataFrames into their respective tables in the database.

    Args:
        crypto_df (DataFrame): formatted crypto metadata dataframe.
    """
    with sqlite3.connect(DB_PATH) as conn:
        # NOTE: save crypto df to crypto table
        # TODO: think about whether it's more efficient to replace or fail "if_exists"
        # crypto_df.to_sql("crypto", conn, if_exists="append", index=False)

        curs = conn.cursor()
        for _, row in crypto_df.iterrows():
            # curs.execute("SELECT symbol FROM crypto WHERE symbol=?", row["symbol"])
            # if curs.fetchone() is None:
            curs.execute("INSERT OR IGNORE INTO crypto VALUES (?, ?)", (row))
