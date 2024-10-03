# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "mysql://root@localhost/imogo"
SQLALCHEMY_DATABASE_URL = "mysql://quadr767_juca:7b5a67574d8b1d77d2803b24946950f0@mysql.imogo.com.br/quadr767_imogo_juca"


engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
