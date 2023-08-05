import bonobo
from extraction import extract
from transformation import transform
from loading import load_crypto, load_crypto_data
from db import initialize_db


def get_graph(**options):
    graph = bonobo.Graph()

    # NOTE: approach 1 -- one transformer
    graph.add_chain(extract, transform)
    # graph.add_chain(transform, _input=extract)

    graph.add_chain(load_crypto, _input=transform)  # loading df_crypto
    graph.add_chain(load_crypto_data, _input=transform)  # loading df_crypto_data

    # NOTE: approach 2 -- two transformers
    # graph.add_chain(extract, transform_crypto, load_crypto)
    # graph.add_chain(extract, transform_crypto_data, load_crypto_data)
    return graph


if __name__ == "__main__":
    initialize_db()
    bonobo.run(get_graph())
