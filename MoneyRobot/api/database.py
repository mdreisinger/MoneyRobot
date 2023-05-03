"""
database.py
"""
# pylint:disable=wrong-import-position

import pathlib
import sys
cur_dir = pathlib.Path(__file__).parent.resolve()
sys.path.append(f"{cur_dir}/..")

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# pylint:disable=relative-beyond-top-level
from .db_info import get_db_info


rds_host, username, password, db_name = get_db_info()

SQLALCHEMY_DATABASE_URL = f"mysql://{username}:{password}@{rds_host}:3306/{db_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
