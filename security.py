import sys
import os
dirname = os.path.dirname(__file__)
 
sys.path.append(dirname)
sys.path.append(dirname+"/db_models/")
from sqlalchemy import create_engine, select, join, MetaData, Table

#from db_models.emergency_call import EmergencyCalls
#from db_models.establishment import Establishments
from db_models.reporters import Reporters
from config_vars import BBDD_CONNECTION
class Security:
    print("starting")
    engine = create_engine(BBDD_CONNECTION)
    connection = engine.connect()
    print("finished connection")
    metadata = MetaData()

    def get_reporters(self):
        query = Reporters.all_reporters()
        return self.connection.execute(query).fetchone()
