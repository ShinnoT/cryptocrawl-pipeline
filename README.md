# Cryptocurrency Crawl Data Pipeline

This project extracts cryptocurrency data from Yahoo Finance, processes the data, and stores the results in a SQLite database. It is a simple ETL pipeline implemented using Python and the [Bonobo ETL framework](https://www.bonobo-project.org/).

<div align="center" style="margin-bottom:10px;margin-top:10px;">
    <img src="https://img.shields.io/badge/Made%20with-Python-green" />
    <img src="https://img.shields.io/badge/Powered%20by-bonobo-black" />
    <img src="https://img.shields.io/badge/Parsed%20with-BeautifulSoup-orange" />
    <img src="https://img.shields.io/badge/Database-SQLite-blue" />
</div>

![cryptocrawl-pipeline - portfolio site](https://github.com/ShinnoT/cryptocrawl-pipeline/assets/26269548/745b43f5-33de-4955-ac7a-4c0ce5e54568)

---

## Table of Contents

-   [About](#about)
-   [Installation](#installation)
-   [Usage](#usage)
-   [License](#license)

---

## About

The script will scrape crypto data from the target website, process the data, and store the results in a SQLite database located at `database/crypto.db`.

You can view the database using any SQLite database client.

---

## Installation

Before running the project, you need to install the required Python libraries. To do this, navigate to the project directory and run the following command:

```bash
pip install -r requirements.txt
```

### NOTE:

_`from collections import Iterable` has been deprecated but is still in use in the bonobo package -- to fix for local usage, modify the import statement in the file `bonobo\config\processors.py` to `from collections.abc import Iterable`_

---

## Usage

To run the ETL pipeline, execute the main script from the project directory:

```bash
python scripts/main.py
```

---

## License

This project is licensed under the terms of the MIT license.

---

<p align="center">Made with ❤️ by Shinno Taguchi</p>
