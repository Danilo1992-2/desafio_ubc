import sys
import os

diretorio_atual = os.path.dirname(os.path.realpath(__file__))
caminho_pai = os.path.abspath(os.path.join(diretorio_atual, '..'))
sys.path.append(caminho_pai)

import pandas as pd

from commands.processar_arquivo import processar_arquivo


def test_processa_arquivo():
    df = pd.DataFrame({
            "nome do aluno":["Alice","Alice","Alice","Alice"],
            "idadé":["10","10","10","10"],
            "Serie":["5","5","5","5"],
            "Nota media":["8.5","8.5","8.5","8.5"],
            "endereço":["123 Main St","123 Main St","123 Main St","123 Main St"],
            "Nome do Pai":["John Doe","John Doe","John Doe","John Doe"],
            "nome da mae":["Jane Doe","Jane Doe","Jane Doe","Jane Doe"],
            "data de nascimento":["2013-05-15T00:00:00Z","2013-05-15T00:00:00Z","2013-05-15T00:00:00Z","2013-05-15T00:00:00Z"]})
    df_processado = processar_arquivo(df, "Arquivo_teste.teste")
    
    assert df.columns[0] == "nome_do_aluno"
    assert df.columns[1] == "idade"
    assert df.columns[2] == "serie"
    assert df.columns[3] == "nota_media"
    assert df.columns[4] == "endereco"
    assert df.columns[5] == "nome_do_pai"
    assert df.columns[6] == "nome_da_mae"
    assert df.columns[7] == "data_de_nascimento"