from logs.model.tabela_logs import Log, db


def add_log(tipo: str, processo: str, menssagem: str, arquivo_nome: str) -> None:
    log = Log(
        tipo=tipo, processo=processo, menssagem=menssagem, nome_arquivo=arquivo_nome
    )
    db.add(log)
    db.commit()
