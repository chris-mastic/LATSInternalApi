import os
import oracledb
from sqlalchemy import create_engine


class OracleDBConnection:
    """
    This is a Singleton Class that is implemented as a base class.
    """
    __instance = None

    @staticmethod
    def getInstance():
        if OracleDBConnection.__instance == None:
            OracleDBConnection()
        return OracleDBConnection.__instance

    def __init__(self):

        if OracleDBConnection.__instance != None:
            raise Exception("This class is a singleton")
        else:
            # Database Credentials
            username = os.getenv("PYTHON_USERNAME")
            password = os.getenv("PYTHON_PASSWORD")
            print(f"username {username}")
            cp = oracledb.ConnectParams()

            cp.parse_connect_string(os.getenv("PYTHON_CONNECTSTRING"))
            print(f"cp {cp}")
            print("after cp.parse")
            # For the default, python-oracledb Thin mode that doesn't use Oracle Instant Client
            thick_mode = None

            OracleDBConnection.__instance = self
            self.engine = create_engine(
                f'oracle+oracledb://{username}:{password}@{cp.host}:{cp.port}/?service_name={cp.service_name}',
                thick_mode=thick_mode)
            print(f"self.enging {self.engine}")
