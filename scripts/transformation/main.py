from bs4 import BeautifulSoup
import pandas as pd
from typing import Tuple

from .helpers import format_html


def transform(soup: BeautifulSoup) -> Tuple[pd.DataFrame, pd.DataFrame]:
    """Transforms raw html soup into clean data in pandas DataFrame.

    Args:
        soup (BeautifulSoup): raw html soup of crawled webpage.

    Returns:
        tuple[DataFrame]: formatted crypto and crypto_data df.
    """
    crypto_df, crypto_data_df = format_html(soup)

    return {"crypto_df": crypto_df, "crypto_data_df": crypto_data_df}
