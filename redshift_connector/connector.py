import os
import psycopg2

import logging.config
from redshift_connector.logging_conf import LOGGING_CONFIG

logging.config.dictConfig(LOGGING_CONFIG)
_logger = logging.getLogger('__name__')


def connect(query):
    try:
        conn = psycopg2.connect(
            host=os.environ.get("ARG_REDSHIFT_SERVER"),
            port=5439,
            user=os.environ.get("ARG_REDSHIFT_USERNAME"),
            password=os.environ.get("ARG_REDSHIFT_PASSWORD"),
            dbname=os.environ.get("ARG_REDSHIFT_DATABASE"),
        )
        _logger.info(
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
        _logger.info(
            "Connection closed and cursor closed")