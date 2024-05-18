from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, select, join, MetaData, Table, Column, Integer
from config_vars import BBDD_CONNECTION
from sqlalchemy import func, desc,text


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
            .join(cls.emc, cls.emc_est, cls.emc_est.c.emc_id == cls.emc.c.inc_id)
            .join(cls.est, cls.emc_est, cls.est.c.est_id == cls.emc_est.c.est_id)
            .where(cls.est.c.est_id == est_id)
            )
        return query
    
    @classmethod
    def most_frequent_accident(cls):
        query = (
            select([cls.emc.c.emc_details, func.count().label('count')])
            .group_by(cls.emc.c.emc_details)
            .order_by(desc('count'))
        )
        
        result = cls.engine.execute(query)
        most_common = result.first()

        result.close()
        return most_common[0] if most_common else None
    @classmethod
    def calls_by_reporter_id(cls, rep_id):
        emergen_report_table = Table("emergen_report", cls.metadata, autoload=True, autoload_with=cls.engine,schema='seguridad')
        query = (
            select([cls.emc])
            .select_from(
                cls.emc
                .join(emergen_report_table, cls.emc.c.emc_id == emergen_report_table.c.emc_id)
            )
            .where(emergen_report_table.c.rep_id == rep_id)
        )
        
        return query
    
    @classmethod
    def calls_by_date_range(cls, start_date, end_date):
        query = (
            select([cls.emc])
            .where(cls.emc.c.emc_date >= start_date)
            .where(cls.emc.c.emc_date <= end_date)
        )
        return query