import pysolr

SOLR_URL = "http://localhost:8983/solr/core_main_3"
SOLR_CON = pysolr.Solr(SOLR_URL, always_commit=True)
