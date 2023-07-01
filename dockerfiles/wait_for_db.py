import os
import time

import psycopg2
from dotenv import load_dotenv

load_dotenv()


def wait_for_db():
    while True:
        try:
            conn = psycopg2.connect(
                host=os.getenv('SQL_HOST'),
                port=os.getenv('SQL_PORT'),
                user=os.getenv('SQL_USER'),
                password=os.getenv('SQL_PASSWORD'),
                dbname=os.getenv('SQL_DATABASE')
            )
            conn.close()
            break
        except psycopg2.OperationalError:
            print('Waiting for the database to start...')
            time.sleep(1)


wait_for_db()
