import logging
import re

from bs4 import BeautifulSoup

from .helpers import format_metadata, request_url


# TODO: use `yield` instead of `return` to iterate over html table pages
def extract() -> BeautifulSoup:
    """Extracts raw page from https://finance.yahoo.com/crypto

    Returns:
        BeautifulSoup: raw html of page.
    """

    try:
        soup_path = "C:\\Users\\User\\Documents\\Code\\cryptocrawl-pipeline\\soup.html"

        initial_soup = request_url(offset=0, count=100)
        # print(soup.prettify(), file=open("soup.html", "a"))

        # with open(soup_path, "r") as f:
        #     soup = BeautifulSoup(f.read(), "html.parser")

        metadata = format_metadata(initial_soup)
        match = re.search(r"of (\d+) results", metadata)
        if match:
            total_rows = int(match.group(1))
        print(total_rows)
        quotient, remainder = divmod(total_rows, 100)

        for i in range(quotient + 1):
            offset = i * 100
            print("iteration:: ", i + 1)
            print("offset:: ", offset)

            # NOTE: last page of table where the remainder (less than hundred rows as we are dividing by 100) logic goes below
            # NOTE: however it seems the Yahoo Finance's last page to display the remainder is broken so SKIPPING FOR NOW
            if i == quotient:
                # TODO: this is the last page (do something with the remainder)
                continue
            else:
                soup = request_url(offset=offset, count=100)
                yield soup
    except Exception as err:
        print("this is the printed error:: ", str(err))
        # logging.exception(str(err))
