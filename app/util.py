import pysolr
import os
import logging


SOLR_URL = os.environ.get("SOLR_CON")
SOLR_CON = pysolr.Solr(SOLR_URL, always_commit=True)


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='logs/todos_logs.log',
                    filemode='w')
