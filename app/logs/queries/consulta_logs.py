from logs.model.tabela_logs import db, Log


def todos_logs() -> "list[Log]":
    consulta = db.query(Log).all()
    return consulta
