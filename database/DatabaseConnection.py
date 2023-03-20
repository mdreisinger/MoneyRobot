"""
Code to create a connection to the Database.
"""

import json
import os
import sys

from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
import botocore
import botocore.session
import pymysql


def get_connection():
    """
    Create a connection to the DB and return the connection.
    """
    rds_host = os.getenv("RDS_HOST")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    db_name = os.getenv("DB_NAME")

    if rds_host and username and password and db_name:
        print("Using environment variables for database connection info!")
    else:
        print("Creating boto client to secretsmanager to get database connection info!")
        client = botocore.session.get_session().create_client('secretsmanager',
                                                              region_name='us-west-2')
        cache_config = SecretCacheConfig()
        cache = SecretCache( config = cache_config, client = client)
        secret = json.loads(cache.get_secret_string('moneyrobot-dev-secret'))
        rds_host  = secret["host"]
        username = secret["username"]
        password = secret["password"]
        db_name = secret["dbname"]

    print(f"Connecting to {db_name} on {rds_host}!")
    try:
        conn = pymysql.connect(host=rds_host,
                               user=username,
                               passwd=password,
                               db=db_name,
                               connect_timeout=10)
    except pymysql.MySQLError as error:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(error)
        sys.exit()
    print("SUCCESS: Connection to RDS MySQL instance succeeded")

    return conn
