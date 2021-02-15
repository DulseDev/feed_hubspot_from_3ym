import psycopg2
import requests
import os

def get_conn_cursor():
    DULSEDB_DBNAME = os.getenv('DULSEDB_DBNAME')
    DULSEDB_USER = os.getenv('DULSEDB_USER')
    DULSEDB_PASSWORD = os.getenv('DULSEDB_PASSWORD')
    DULSEDB_HOST = os.getenv('DULSEDB_HOST')
    DULSEDB_PORT = os.getenv('DULSEDB_PORT')
    try:
        conn = psycopg2.connect(dbname=DULSEDB_DBNAME,
                user=DULSEDB_USER,
                password=DULSEDB_PASSWORD,
                host=DULSEDB_HOST,
                port=DULSEDB_PORT)
        cursor = conn.cursor()
    except Exception as e:
        raise e
    return conn, cursor

# var data can be request for quote OR quote OR order from 3ym
def is_in_hubspot(data, deals):
    for deal in deals:
        if deal['name'] == data['fullNumber']
            return True
    return False

def log_db_create_rfq_hubspot(data, type, conn, cursor):
