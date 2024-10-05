from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = "mysql://quadr767_juca:7b5a67574d8b1d77d2803b24946950f0@mysql.imogo.com.br/quadr767_imogo_juca"

# Adiciona configurações para melhorar a gestão da pool de conexões
engine = create_engine(
    SQLALCHEMY_DATABASE_URL,
    pool_size=10,           # Número máximo de conexões
    max_overflow=20,         # Número máximo de conexões extras
    pool_pre_ping=True,      # Verifica a conexão antes de usá-la
    pool_recycle=280         # Recicla a conexão após 280 segundos de inatividade
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
