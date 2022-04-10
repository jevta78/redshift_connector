import os
import psycopg2

def connect():
    try:
        print(os.environ.get("ARG_REDSHIFT_SERVER"))
        print(os.environ.get("ARG_REDSHIFT_USERNAME"))
        conn = psycopg2.connect(
            host=os.environ.get("ARG_REDSHIFT_SERVER"),
            port=5439,
            user=os.environ.get("ARG_REDSHIFT_USERNAME"),
            password=os.environ.get("ARG_REDSHIFT_PASSWORD"),
            dbname=os.environ.get("ARG_REDSHIFT_DATABASE"),
        )
        return conn.cursor()
    except Exception as err:
        print(err)