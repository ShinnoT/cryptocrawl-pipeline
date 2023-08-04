from typing import Dict

import pandas as pd

from .helpers import save_to_db


def load(data: Dict[pd.DataFrame, pd.DataFrame]):
    """Saves transformed clean data to database.

    Args:
        data (Dict): a dictionary of dataframes containing crypto_df and crypto_data_df.
    """
    save_to_db(**data)
