from util import SOLR_CON
from logs.commands.inserir_logs import add_log


def grava_dados_solr(dados: "list[dict]", arquivo_nome: str) -> str:
    try:
        if SOLR_CON.ping():
            SOLR_CON.add(dados)
            add_log("Info", "Envia dados pro Solr", "Enviado", arquivo_nome)
            return "OK"
    except Exception as e:
        add_log("Erro", "Envia dados pro Solr", str(e), arquivo_nome)
        return str(e)
