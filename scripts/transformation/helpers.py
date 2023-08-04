import locale
import time
from typing import Tuple

import pandas as pd
from bs4 import BeautifulSoup

locale.setlocale(locale.LC_ALL, "")


def format_float(value):
    if value[-1] == "%":
        return locale.atof(value[1:-1])
    if value[0] == "-" or value[0] == "+":
        return locale.atof(value[1:])
    return locale.atof(value)


def format_text_float(value):
    tens = {"K": 10e3, "M": 10e6, "B": 10e9, "T": 10e12, "Q": 10e15}

    if not value[-1] in tens:
        return locale.atof(value)

    factor, exp = value[0:-1], value[-1].upper()
    return float(factor) * tens[exp]


def format_table(raw_soup: BeautifulSoup) -> pd.DataFrame:
    """Finds and formats raw html table into pandas DataFrame.

    Args:
        raw_soup (BeautifulSoup): html parsed raw body of entire web page.

    Returns:
        pd.DataFrame: crypto table on html as a DataFrame.
    """
    table = raw_soup.find("div", {"id": "scr-res-table"}).find("table")
    table_columns = [
        column_header.text.strip() for column_header in table.thead.tr.find_all("th")
    ]
    table_df = pd.DataFrame(columns=table_columns)

    for row in table.tbody.find_all("tr"):
        df_row = [table_cell.text.strip() for table_cell in row.find_all("td")]
        table_df.loc[len(table_df)] = df_row

    # NOTE: split table_df into 2 dataframes crypto_df && crypto_data
    crypto_df = pd.DataFrame().assign(symbol=table_df["Symbol"], name=table_df["Name"])
    crypto_data_df = pd.DataFrame().assign(
        crypto_symbol=table_df["Symbol"],
        price=table_df["Price (Intraday)"].apply(format_float),
        change_value=table_df["Change"].apply(format_float),
        change_percent=table_df["% Change"].apply(format_float),
        market_cap=table_df["Market Cap"].apply(format_text_float),
        volume_in_currency=table_df["Volume in Currency (Since 0:00 UTC)"].apply(
            format_text_float
        ),
        volume_in_currency_day=table_df["Volume in Currency (24Hr)"].apply(
            format_text_float
        ),
        total_volume_all_currencies=table_df[
            "Total Volume All Currencies (24Hr)"
        ].apply(format_text_float),
        circulating_supply=table_df["Circulating Supply"].apply(format_text_float),
        currency="USD",
        timestamp=time.time(),
    )

    return crypto_df, crypto_data_df


def format_html(soup: BeautifulSoup) -> Tuple[pd.DataFrame, pd.DataFrame, pd.DataFrame]:
    """Reads parsed html soup and extracts table metadata & table DataFrame.

    Args:
        soup (BeautifulSoup): html parsed raw body of entire web page.

    Returns:
        tuple: (table_metadata: str, crypto_df: DataFrame, crypto_data_df: DataFrame)
    """
    crypto_df, crypto_data_df = format_table(soup)
    return crypto_df, crypto_data_df
