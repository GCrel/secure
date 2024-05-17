from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, join, MetaData, Table, Column, Integer
from config_vars import BBDD_CONNECTION

Base = declarative_base()

class Reporters (Base):
    __tablename__ = "reporters"
    print("entering Establishment config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    rep = Table("reporters", metadata, schema='seguridad', autoload=True, autoload_with=engine)
    id_not_in_db = Column(Integer, primary_key=True) # Tabla con primary key
    print("finished config for Establishment")

    @classmethod
    def all_reporters(cls):
        query = select([cls.rep])
        return query
    
    @classmethod
    def single_reporter(cls, rep_id):
        query = select([cls.rep]).where(cls.rep.c.rep_id == rep_id)
        return query
    