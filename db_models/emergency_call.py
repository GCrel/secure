from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, join, MetaData, Table, Column, Integer
from config_vars import BBDD_CONNECTION

Base = declarative_base()

class EmergencyCalls(Base):
    __tablename__ = "emergency_calls"
    print("entering Emergency Calls config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    emc = Table("emergency_calls", metadata, autoload=True, autoload_with=engine, schema='seguridad')
    id_not_in_db = Column(Integer, primary_key=True) # Tabla con primary key
    print("finished config for Emergency Calls")

    @classmethod
    def all_calls(cls):
        queri = select([cls.emc])
        return queri
    
    @classmethod
    def single_call(cls, *, emc_id):
        query = select([cls.emc]).where(cls.emc.c.emc_id == emc_id)
        return query