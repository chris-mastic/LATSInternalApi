
from flask import current_app
import logging
import os
import oracledb
from sqlalchemy import create_engine


class OracleDBConnection:
    """
    This is a Singleton Class that is implemented as a base class.
    """
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._initialize()
        return cls.__instance

    def _initialize(self):
        # Database Credentials
        username = current_app.config["ORACLE_USERNAME"]
        password = current_app.config["ORACLE_PASSWORD"]
        connection_string = current_app.config["ORACLE_CONNECTSTRING"]

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

        cp.parse_connect_string(connection_string)

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
