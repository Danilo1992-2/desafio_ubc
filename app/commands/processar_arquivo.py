import pandas as pd
from unidecode import unidecode
from logs.commands.inserir_logs import add_log


def processar_arquivo(df: pd.DataFrame, arquivo_nome: str) -> pd.DataFrame:
    try:
        nome_colunas: list[str] = df.columns
        df.columns: pd.DataFrame = [formatar_nome_coluna(nome_coluna) for nome_coluna in nome_colunas]
        df: pd.DataFrame = df.fillna("")
        add_log("Info", "processamento de arquivo", "Processado", arquivo_nome)
        return df
    except Exception as e:
        add_log("Erro", "processamento de arquivo", str(e), arquivo_nome)

def formatar_nome_coluna(palavra: str) -> str:
    palavra_formatada: str = unidecode(palavra).replace(" ", "_").lower()
    return palavra_formatada
