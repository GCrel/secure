from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, join, MetaData, Table, Column, Integer
from config_vars import BBDD_CONNECTION

Base = declarative_base()

class Incidents (Base):
    __tablename__ = "incidents"
    print("entering Establishment config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    inc = Table("incidents", metadata, autoload=True, autoload_with=engine, schema='seguridad')

    id_not_in_db = Column(Integer, primary_key=True) # Tabla con primary key
    print("finished config for Establishment")

    @classmethod
    def all_incidents(cls):
        queri = select([cls.inc])
        return queri
    
    @classmethod
    def single_incident(cls, inc_id):
        queri = select([cls.inc]).where(cls.inc.c.inc_id == inc_id)
        return queri
    
    