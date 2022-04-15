import os
from telnetlib import ENCRYPT
from dotenv import load_dotenv

load_dotenv() #Carga en memoria las variables de entorno definidas en .env

class Config:
    SERVER_NAME = "localhost:5001"
    DEBUG = True

    DATABASE_PATH = "app/database/contact_book.db"
    DATABASE_PATH_MYSQL = "mysql+pymysql://root:CAMIlodev1994@localhost/pets"
    DB_TOKEN = os.environ.get("DB_TOKEN")
    ENCRYPT_DB = True

    TEMPLATE_FOLDER = "views/templates/"
    STATIC_FOLDER = "views/static/"

