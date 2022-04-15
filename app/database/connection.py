from contextlib import contextmanager
from typing import Any, Iterator, List, Optional
from flask_sqlalchemy import SQLAlchemy, create_engine
from config import Config
from .security import _encrypt_decrypt
from app import db

# DATABASE_PATH = Config.DATABASE_PATH

# @contextmanager
# def __get_cursor():
#     engine = create_engine(DATABASE_PATH)
#     connection = engine.connect()
#     cursor = connection.cursor()
#     try:
#         yield cursor
#         connection.commit()
#     finally:
#         cursor.close()
#         connection.close()

# def _fetch_one(query, parameters=None):
#     if parameters is None:
#         parameters = []
    
#     with __get_cursor() as cursor:
#         cursor.execute(query, parameters)
#         return cursor.fetchone()

# def _fetch_all(query, parameters=None):
#     if parameters is None:
#         parameters = []
#     with __get_cursor() as cursor:
#         cursor.execute(query, parameters)
#         return cursor.fetchall()


# def _fetch_none(query, parameters=None):
#     if parameters is None:
#         parameters = []
#     with __get_cursor() as cursor:
#         cursor.execute(query, parameters)
#         return None


# def _fetch_lastrow_id(query, parameters=None):
#     if parameters is None:
#         parameters = []
    
#     with __get_cursor() as cursor:
#         cursor.execute(query, parameters)
#         return cursor.lastrowid()


