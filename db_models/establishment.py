from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, join, MetaData, Table, Column, Integer
from config_vars import BBDD_CONNECTION

Base = declarative_base()

class Establishments (Base):
    __tablename__ = "establishment"
    print("entering Establishment config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    est = Table("establishment", metadata, autoload=True, autoload_with=engine, schema='seguridad')
    id_not_in_db = Column(Integer, primary_key=True) # Tabla con primary key
    print("finished config for Establishment")

    @classmethod
    def all_establishments(cls):
        queri = select([cls.est])
        return queri
    
    @classmethod
    def single_establishment(cls, est_id):
        queri = select([cls.est]).where(cls.est.c.est_id == est_id)
        return queri

    