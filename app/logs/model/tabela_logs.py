from sqlalchemy import create_engine

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


path_logs = 'logs/logs.db'
ENGINE = create_engine(f'sqlite:///{path_logs}', connect_args={"check_same_thread": False})

Base = declarative_base()

class Log(Base):
    __tablename__ = 'logs'

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    tipo = Column(String)
    processo = Column(String)
    menssagem = Column(String)
    nome_arquivo = Column(String)

Base.metadata.create_all(bind=ENGINE)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=ENGINE)
db = SessionLocal()
