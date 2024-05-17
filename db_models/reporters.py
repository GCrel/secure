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
    
    @classmethod
    def reporter(cls, inc_id):
        query = select([cls.rep]).select_from(
        join(cls.rep, cls.emc, cls.rep.c.rep_id == cls.emc.c.rep_id)
        .join(cls.emc, cls.emergency_reports.c.emc_id == cls.emc.c.emc_id)
        ).where(cls.emc.c.inc_id == inc_id)
        return query