#from sqlalchemy import create_engine, select, join, MetaData, Table
import sys
import os
dirname = os.path.dirname(__file__)
 
sys.path.append(dirname)
sys.path.append(dirname+"/db_models/")

from sqlalchemy import create_engine, select, join, MetaData, Table
from sqlalchemy import create_engine, select, join, MetaData, Table
from db_models.emergency_call import EmergencyCalls
from db_models.establishment import Establishments
from db_models.reporters import Reporters
from db_models.incidents import Incidents
from config_vars import BBDD_CONNECTION
class Security:
    print("starting")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    print("finished connection")
    metadata = MetaData()

    def get_reporters(self,*,rep_id=None):
        if rep_id:
            query = Reporters.single_reporter(rep_id)
        else:
            query = Reporters.all_reporters()
        return self.connection.execute(query).fetchall()

    def get_emergency_call(self,* ,emc_id=None,inc_id=None,est_id=None):
        if emc_id:
            query = EmergencyCalls.single_call(emc_id)
        elif inc_id:
            query = EmergencyCalls.calls_by_incident(inc_id)
        elif est_id:
            query = EmergencyCalls.call_by_establishment(est_id)
        else:
            query = EmergencyCalls.all_calls()
        return self.connection.execute(query).fetchall()

    def get_incidents(self,* ,inc_id=None):
        if inc_id:
            query = Incidents.single_incident(inc_id)
        else:
            Incidents.all_incidents()
        return self.connection.execute(query).fetchall()
    
    def get_establishment(self, *, est_id=None):
        if est_id:
            query = Establishments.single_establishment(est_id)
        else:
            query = Establishments.all_establishments()
        return self.connection.execute(query).fetchall()
