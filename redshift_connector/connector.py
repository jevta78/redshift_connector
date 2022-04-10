import os
import psycopg2
import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
handler = logging.StreamHandler()
c_format = logging.Formatter('%(name)s - %(levelname)s - %(message)s')
handler.setFormatter(c_format)
logger.addHandler(handler)

def connect(query):
    try:
        conn = psycopg2.connect(
            host=os.environ.get("ARG_REDSHIFT_SERVER"),
            port=5439,
            user=os.environ.get("ARG_REDSHIFT_USERNAME"),
            password=os.environ.get("ARG_REDSHIFT_PASSWORD"),
            dbname=os.environ.get("ARG_REDSHIFT_DATABASE"),
        )
        logger.info(
            "Connection established")


        cursor=conn.cursor()
        cursor.execute(query)
        rows = cursor.fetchall()
        return cursor, rows

    except Exception as err:
        print(err)

    finally:
        conn.close()
        cursor.close()
        logger.info(
            "Connection closed and cursor closed")