import sys
import os

diretorio_atual = os.path.dirname(os.path.realpath(__file__))
caminho_pai = os.path.abspath(os.path.join(diretorio_atual, '..'))
sys.path.append(caminho_pai)

from util import SOLR_CON


SOLR_ALL = SOLR_CON.search('*:*')

def qtd_registros() -> int:
    qtd: int = SOLR_CON.search('*:*')
    return qtd.hits

def qtd_alunos_agrupado(dado: str) -> 'list[dict]':
    params = {
        'q': '*:*',
        'rows': 0,
        'facet': 'true',
        'facet.field': dado,
    }
    resultado = SOLR_CON.search(**params)
    serie_agrupado = resultado.facets['facet_fields'][dado]
    return lista_pra_dict(serie_agrupado)


def lista_pra_dict(lista: 'list[str, int]') -> dict:
    dicionario: dict = {}
    for item in range(0, len(lista), 2):
        if item + 1 < len(lista):
            dicionario.update( { lista[item] : lista[item + 1] } )
    return dicionario
