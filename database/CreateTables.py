#pylint:disable=invalid-name
"""
Code to create tables in moneyrobot db given sql file.
"""

import json
import logging
import os
import sys

from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
import botocore
import botocore.session
import pymysql

client = botocore.session.get_session().create_client('secretsmanager')
cache_config = SecretCacheConfig()
cache = SecretCache( config = cache_config, client = client)

secret = json.loads(cache.get_secret_string('moneyrobot-dev-secret'))
RDS_HOST = os.getenv("RDS_HOST")
USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
DB_NAME = os.getenv("DB_NAME")

rds_host  = RDS_HOST if RDS_HOST else secret["host"]
user_name = USERNAME if USERNAME else secret["username"]
password = PASSWORD if PASSWORD else secret["password"]
db_name = DB_NAME if DB_NAME else secret["dbname"]

logger = logging.getLogger()
logger.setLevel(logging.INFO)

def create_tables():
    """
    This function creates new tables in our RDS instance.
    """
    try:
        conn = pymysql.connect(host=rds_host,
                               user=user_name,
                               passwd=password,
                               db=db_name,
                               connect_timeout=5)
    except pymysql.MySQLError as error:
        logger.error("ERROR: Unexpected error: Could not connect to MySQL instance.")
        logger.error(error)
        sys.exit()
    logger.info("SUCCESS: Connection to RDS MySQL instance succeeded")

    with open('create_tables.sql', 'r', encoding='utf-8') as sql_file:
        sql_commands = sql_file.read().split(";")

    with conn.cursor() as cur:
        for command in sql_commands:
            cur.execute(command)
            conn.commit()

        cur.execute("show tables")
        logger.info("The following tables have been added to the database:")
        for row in cur:
            logger.info(row)
    conn.commit()
