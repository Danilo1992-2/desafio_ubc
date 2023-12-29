from app.util import SOLR_CON
from time import sleep


def test_grava_dados_no_solr():
    dict_test: dict = {
        "nome": "Nome_teste",
        "idade": 11,
        "serie": 6,
        "nota_media": 7.2,
        "endereco": "456 Oak St",
        "nome_do_pai": "Bob Smith",
        "nome_da_mae": "Alice Smith",
        "data_de_nascimento": "2012-08-21T00:00:00Z",
    }
    SOLR_CON.add(dict_test)
    results = SOLR_CON.search(f"nome:{dict_test['nome']}")
    resultado = results.docs[0]
    assert resultado["nome"] != None
