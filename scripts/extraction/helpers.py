from bs4 import BeautifulSoup
from requests import request
from settings import BASE_URL


# NOTE: Yahoo finance blocks non-human quests that are not made through a browser
# NOTE: user-agent header needs to be changed for query params to work as this mimics browser interaction
def request_url(offset: int, count: int = 100) -> BeautifulSoup:
    """Requests the raw unparsed html content from the Yahoo Finance Crypto website.

    Args:
        offset (int): pagination of html table.
        count (int, optional): number of rows to load on html table. Defaults to 100.

    Returns:
        BeautifulSoup: html parsed raw body of entire web page.
    """
    request_params = {"count": count, "offset": offset}
    headers = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36"
    }
    response = request("GET", url=BASE_URL, params=request_params, headers=headers)
    return BeautifulSoup(response.text, "html.parser")


def format_metadata(raw_soup: BeautifulSoup) -> str:
    """Fetches html table metadata (i.e. \"1-100 of 10086 results\").

    Args:
        raw_soup (BeautifulSoup): html parsed raw body of entire web page.

    Returns:
        str: html metadata (i.e. \"1-100 of 10086 results\").
    """
    table_results = raw_soup.find("span", {"class": "Mstart(15px) Fw(500) Fz(s)"})
    return table_results.span.text.strip()
