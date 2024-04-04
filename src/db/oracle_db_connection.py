import logging
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
            username = os.getenv("ORACLE_USERNAME")
            password = os.getenv("ORACLE_PASSWORD")
            cp = oracledb.ConnectParams()

            logger = logging.getLogger(__name__)
            logger.setLevel(logging.DEBUG)

            # setup a handler to allow you to write to sepearate log file than what was created using basicConfig()
            # all of available Handlers (HTTP, email, etc)
            handler = logging.FileHandler('db_connection.log', 'a')
            # setup a formatter
            formatter = logging.Formatter(
                '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            handler.setFormatter(formatter)
            logger.addHandler(handler)
            logger.info("creating OracleDBConnection instance...")

            cp.parse_connect_string(os.getenv("ORACLE_CONNECTSTRING"))

            # For the default, python-oracledb Thin mode that doesn't use Oracle Instant Client
            thick_mode = None

            OracleDBConnection.__instance = self
            try:

                self.engine = create_engine(
                    f'oracle+oracledb://{username}:{password}@{cp.host}:{cp.port}/?service_name={cp.service_name}',
                    thick_mode=thick_mode)
            except Exception as e:
                logger.error(
                    f"oracle_db_connection.OracleDBConnection error: Unable to connect to the database: {str(e)}")
