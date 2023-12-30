from unidecode import unidecode

import pandas as pd

from logs.commands.inserir_logs import add_log


def processar_arquivo(df: pd.DataFrame, arquivo_nome: str) -> pd.DataFrame:
    try:
        nome_colunas: list[str] = df.columns
        df: pd.DataFrame = valida_primeira_coluna(df)
        df.columns: pd.DataFrame = [
            formatar_nome_coluna(nome_coluna) for nome_coluna in nome_colunas
        ]
        df: pd.DataFrame = df.fillna("")
        df: pd.DataFrame = defenir_tipos(df)
        add_log("Info", "processamento de arquivo", "Processado", arquivo_nome)
        return df
    except Exception as e:
        add_log("Erro", "processamento de arquivo", str(e), arquivo_nome)


def formatar_nome_coluna(palavra: str) -> str:
    palavra_formatada: str = unidecode(palavra).replace(" ", "_").lower()
    return palavra_formatada


def valida_primeira_coluna(df: pd.DataFrame) -> pd.DataFrame:
    qtd_coluna_1 = len(df.iloc[0, 0].split(","))
    if qtd_coluna_1 > 1:
        df: pd.DataFrame = df[df.columns[0]].str.replace('"', "", regex=True)
        df: pd.DataFrame = pd.DataFrame([linhas.split(",") for linhas in df])
        return df
    return df

def defenir_tipos(df: pd.DataFrame) -> pd.DataFrame:
    df_types = {
    df.columns[0]: str,
    df.columns[1]: int,
    df.columns[2]: str,
    df.columns[3]: float,
    df.columns[4]: str,
    df.columns[5]: str,
    df.columns[6]: str,
    df.columns[7]: str}

    df = df.astype(df_types)
    return df
