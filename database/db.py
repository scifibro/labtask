import os

import psycopg2
from dotenv import load_dotenv


load_dotenv("C://Users//sci//Desktop//kaspi_lab_task//secrets.env")


host = os.environ['PG_HOST']
port = os.environ['PG_PORT']
dbname = os.environ['PG_DBNAME']
user = os.environ['PG_USER']
pw = os.environ['PG_PW']


conn = psycopg2.connect(host=host, port=port, dbname=dbname, user=user, password=pw)


db_error = psycopg2.DatabaseError


