import os
from dotenv import load_dotenv
load_dotenv('../.env')

import pyodbc
from sqlalchemy import create_engine

def get_postgres_creds():
    #get password from environmnet var
    pwd = os.getenv('POSTGRES_PASSWORD')
    uid = os.getenv('POSTGRES_USER')
    server = os.getenv('POSTGRES_HOST')
    port = os.getenv('POSTGRES_PORT')
    db =  os.getenv('POSTGRES_DB')

    cs = create_engine(f'postgresql://{uid}:{pwd}@{server}:{port}/{db}')
    try:
        return cs
    except:
        print("Error loading the config file.")