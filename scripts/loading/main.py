from typing import Tuple

import pandas as pd

# from .helpers import save_to_db
from .save_crypto import save_crypto
from .save_crypto_data import save_crypto_data


# data: Tuple[pd.DataFrame, pd.DataFrame]
def load_crypto(*data: pd.DataFrame):
    """Saves transformed clean CRYPTO data to database.

    Args:
        data (Dict): a dictionary of dataframes containing crypto_df and crypto_data_df.
    """
    crypto_df, _ = data
    save_crypto(crypto_df)


# data: Tuple[pd.DataFrame, pd.DataFrame]
def load_crypto_data(*data: pd.DataFrame):
    """Saves transformed clean CRYPTO_DATA data to database.

    Args:
        data (Dict): a dictionary of dataframes containing crypto_df and crypto_data_df.
    """
    _, crypto_data_df = data
    save_crypto_data(crypto_data_df)


# def load(data: Dict[pd.DataFrame, pd.DataFrame]):
#     """Saves transformed clean data to database.

#     Args:
#         data (Dict): a dictionary of dataframes containing crypto_df and crypto_data_df.
#     """
#     save_to_db(**data)
