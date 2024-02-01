import os

import oracledb
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text


class OracleDB:
    __instance = None

    @staticmethod
    def getInstance():
        print("in getInstance")
        if OracleDB.__instance == None:
            print("in if, before OracleDB()")
            OracleDB()
        return OracleDB.__instance
    
    def __init__(self):
        
        if OracleDB.__instance != None:
            raise Exception("This class is a singleton")
        else:
            # Database Credentials
            username = os.environ.get("PYTHON_USERNAME")
            password = os.environ.get("PYTHON_PASSWORD")
            cp = oracledb.ConnectParams()
            cp.parse_connect_string(os.environ.get("PYTHON_CONNECTSTRING"))

            # For the default, python-oracledb Thin mode that doesn't use Oracle Instant Client
            thick_mode = None

            OracleDB.__instance = self
            self.engine =  create_engine(
    f'oracle+oracledb://{username}:{password}@{cp.host}:{cp.port}/?service_name={cp.service_name}',
    thick_mode=thick_mode)
    
