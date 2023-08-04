import bonobo
from extraction import extract
from transformation import transform
from loading import load
from db import initialize_db


def get_graph(**options):
    graph = bonobo.Graph()
    graph.add_chain(extract, transform, load)
    return graph


if __name__ == "__main__":
    initialize_db()
    bonobo.run(get_graph())
