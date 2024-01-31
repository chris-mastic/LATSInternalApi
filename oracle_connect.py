import os

import oracledb
import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy import text
from typing import Any, Dict, Optional


class OracleDB:
    def __init__(self, db_path: str):
        self.db_path = db_path
        self.engine = None
    
    def __enter__(self):
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
        return self

   

    def execute(self, query: str, params: Optional[Dict[str, Any]] = None):
        cursor = self