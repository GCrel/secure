from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, join, MetaData, Table, Column, Integer
from config_vars import BBDD_CONNECTION

from establishment import Establishments

Base = declarative_base()

class EmergencyCalls(Base):
    __tablename__ = "emergency_calls"
    print("entering Emergency Calls config")
    engine = create_engine(BBDD_CONNECTION)
    metadata = MetaData()
    emc = Table("emergency_calls", metadata, autoload=True, autoload_with=engine, schema='seguridad')
    id_not_in_db = Column(Integer, primary_key=True) # Tabla con primary key
    print("finished config for Emergency Calls")

    emc_est = Table("emerg_establis", metadata, autoload=True, autoload_with=engine, schema='seguridad')
    est = Establishments.est

    @classmethod
    def all_calls(cls):
        queri = select([cls.emc])
        return queri
    
    @classmethod
    def single_call(cls, emc_id):
        query = select([cls.emc]).where(cls.emc.c.emc_id == emc_id)
        return query

    @classmethod
    def calls_by_incident(cls,inc_id):
        query = select([cls.emc]).where(cls.emc.c.inc_id ==inc_id)
        return query
    
    @classmethod
    def call_by_establishment(cls, est_id):
        query = (
            select([cls.emc,cls.est.c.est_id])
            .select_from(
                cls.emc
                .join(cls.emc_est, cls.emc.c.emc_id == cls.emc_est.c.emc_id)
                .join(cls.est, cls.emc_est.c.est_id == cls.est.c.est_id)
            )
        .where(cls.est.c.est_id == est_id)
    )
        return query