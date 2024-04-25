import logging
from flask import current_app
from sqlalchemy import create_engine


class MySQLDBConnection:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
            cls.__instance._initialize()
        return cls.__instance

    def _initialize(self):
        # Database Credentials
        user = current_app.config['MYSQL_USER']
        password = current_app.config['MYSQL_PASSWORD']
        host = current_app.config['MYSQL_HOST']
        database = current_app.config['MYSQL_DATABASE']
        port = current_app.config['MYSQL_PORT']

        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)

        # Setup a handler to allow writing to a separate log file
        handler = logging.FileHandler('mysql_connection.log', 'a')
        formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info("Creating MySQLDBConnection instance...")

        try:
            # Create an engine object
            self.engine = create_engine(
                f'mysql+mysqlconnector://{user}:{password}@{host}:{port}/{database}')

        except Exception as e:
            logger.error(
                f"mysql_db_connection.MySQLDBConnection error: Unable to connect to the database: {str(e)}"
            )
