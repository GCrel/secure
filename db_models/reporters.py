from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, join, MetaData, Table, Column, Integer
from config_vars import BBDD_CONNECTION

Base = declarative_base()

class Reporters (Base):
    __tablename__ = "reporters"
    print("entering Establishment config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    rep = Table("reporters", metadata, autoload=True, autoload_with=engine, schema='seguridad')
    id_not_in_db = Column(Integer, primary_key=True) # Tabla con primary key
    print("finished config for Establishment")

    @classmethod
    def all_reporters(rep):
        queri = select([rep.est])
        return queri
    
    @classmethod
    def single_reporter(rep, rep_id):
        queri = select([rep.est]).where(rep.est.c.rep_id == rep_id)
        return queri