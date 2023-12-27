import pandas as pd
from fastapi import File
from unidecode import unidecode
from logs.commands.inserir_logs import add_log


def processar_arquivo(arquivo: File) -> pd.DataFrame:
    try:
        data_frame: pd.DataFrame = pd.read_csv(arquivo, encoding='utf-8')
        nome_colunas: list[str] = data_frame.columns
        data_frame: pd.DataFrame = data_frame["Nome"].str.split(',', expand=True)
        data_frame.columns: pd.DataFrame = [formatar_nome_coluna(nome_coluna) for nome_coluna in nome_colunas]
        data_frame_formatado = data_frame.replace(r'\"', '', regex=True)

        add_log("Sucesso", "processamento de arquivo", "Processado")

        return data_frame_formatado
    except Exception as e:
        add_log("Erro", "processamento de arquivo", e)
        
    
def formatar_nome_coluna(palavra: str) -> str:
    palavra_formatada: str = unidecode(palavra).replace(" ", "_").lower()

    return palavra_formatada
