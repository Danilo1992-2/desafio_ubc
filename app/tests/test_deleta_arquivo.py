from app.commands.deleta_arquivo import remove_arquivo
import os


def test_deleta_arquivo():
    caminho_arquivo: str = "arquivos_leitura/arquivo_text.csv"
    with open(caminho_arquivo, "w") as arquivo_text:
        arquivo_text.write("arquivo teste")
    remove_arquivo(caminho_arquivo)

    assert os.path.exists(caminho_arquivo) != True
