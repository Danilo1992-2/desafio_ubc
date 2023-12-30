import os
import logging

import pysolr


SOLR_URL = os.environ.get("SOLR_CON")
SOLR_CON = pysolr.Solr(SOLR_URL, always_commit=True, timeout=10)


logging.basicConfig(
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filename="logs/todos_logs.log",
    filemode="w",
)
