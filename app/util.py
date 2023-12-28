import pysolr
import logging


SOLR_URL = "http://localhost:8983/solr/core_345/"
SOLR_CON = pysolr.Solr(SOLR_URL, always_commit=True)


logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    filename='app/logs/todos_logs.log',
                    filemode='w')
