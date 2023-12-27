from logs.model.tabela_logs import Log, db


def add_log(tipo: str, processo: str,menssagem: str) -> None:
    log = Log(tipo=tipo, processo=processo, menssagem=menssagem)
    db.add(log)
    db.commit()
