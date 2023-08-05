import logging
from typing import Tuple

import pandas as pd
from bs4 import BeautifulSoup

from .helpers import format_html


def transform(soup: BeautifulSoup) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Transforms raw html soup into clean data in pandas DataFrame.

    Args:
        soup (BeautifulSoup): raw html soup of crawled webpage.

    Returns:
        tuple[DataFrame]: formatted crypto and crypto_data df.
    """
    try:
        crypto_df, crypto_data_df = format_html(soup)

        yield crypto_df, crypto_data_df
    except Exception as err:
        print("this is the printed error:: ", str(err))
        # logging.exception(str(err))
