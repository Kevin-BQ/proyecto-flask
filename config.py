from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ['SQLSERVER_USER']
password = os.environ['SQLSERVER_PASSWORD']
host = os.environ['SQLSERVER_HOST']
database = os.environ['SQLSERVER_DATABASE']

URL_DATABASE = f'mssql+pyodbc://{user}:{password}@{host}/{database}?driver=ODBC+Driver+17+for+SQL+Server'