from commands.processar_arquivo import processar_arquivo
from commands.grava_dados_no_solr import grava_dados_solr
from commands.deleta_arquivo import remove_arquivo
from sys import path
import pandas as pd

def main(arquivo: path):
    chunk_size: int = 10000
    data_frame: pd.DataFrame = pd.read_csv(arquivo, encoding='utf-8', chunksize=chunk_size)
    for df in data_frame:
        try:
            processado: pd.DataFrame = processar_arquivo(df, arquivo)
            grava_dados_solr(processado.to_dict(orient='records'), arquivo)
            remove_arquivo(arquivo)
        except Exception as e:
            print(str(e))
