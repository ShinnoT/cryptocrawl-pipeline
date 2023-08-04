import sqlite3


def create_crypto_table(conn: sqlite3.Connection):
    try:
        sql = """CREATE TABLE IF NOT EXISTS crypto (
                    symbol text PRIMARY KEY,
                    name text NOT NULL
                    ); """
        conn.execute(sql)
    except sqlite3.Error as e:
        print(e)


def create_crypto_data_table(conn: sqlite3.Connection):
    try:
        sql = """CREATE TABLE IF NOT EXISTS crypto_data (
                        id integer PRIMARY KEY,
                        crypto_symbol text NOT NULL,
                        price real,
                        change_value real,
                        change_percent real,
                        market_cap real,
                        volume_in_currency real,
                        volume_in_currency_day real,
                        total_volume_all_currencies real,
                        circulating_supply real,
                        currency text DEFAULT "USD" NOT NULL,
                        timestamp integer NOT NULL,
                        FOREIGN KEY (crypto_symbol) REFERENCES crypto (symbol)
                    ); """
        conn.execute(sql)

        # create index on the timestamp column
        conn.execute(
            "CREATE INDEX IF NOT EXISTS idx_timestamp ON crypto_data (timestamp);"
        )
    except sqlite3.Error as e:
        print(e)


def initialize_db():
    try:
        with sqlite3.connect(
            "database/crypto.db"
        ) as conn:  # creates a SQLite database in the 'database' folder
            print(sqlite3.version)
            create_crypto_table(conn)
            create_crypto_data_table(conn)
    except sqlite3.Error as e:
        print(e)
