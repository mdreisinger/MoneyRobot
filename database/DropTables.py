"""
Code to drop all tables in moneyrobot db given sql file.
"""

import json
import os
import sys

from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
import botocore
import botocore.session
import click
import pymysql


@click.command()
def drop_tables():
    """
    This function drops all tables in our RDS instance.
    The database information it uses can be defined in environment variables:
    RDS_HOST, USERNAME, PASSWORD, DB_NAME.
    If these environment variables are not defined, it will use the information
    defined in 'moneyrobot-dev-secret' in SecretsManager.
    """
    rds_host = os.getenv("RDS_HOST")
    username = os.getenv("USERNAME")
    password = os.getenv("PASSWORD")
    db_name = os.getenv("DB_NAME")

    if rds_host and username and password and db_name:
        print("Using environment variables for database connection info!")
    else:
        print("Creating boto client to secretsmanager to get database connection info!")
        client = botocore.session.get_session().create_client('secretsmanager', region_name='us-west-2')
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
                               connect_timeout=10,
                               cursorclass=pymysql.cursors.DictCursor)
    except pymysql.MySQLError as error:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(error)
        sys.exit()
    print("SUCCESS: Connection to RDS MySQL instance succeeded")

    with conn.cursor() as cur:
        cur.execute("show tables")
        tables = cur.fetchall()
        print(tables)
        cur.execute("SET FOREIGN_KEY_CHECKS = 0")
        for table_dict in tables:
            for table in table_dict.values():
                print(f"Dropping table: {table}")
                cur.execute(f"drop table {table}")
                conn.commit()
        cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    conn.commit()
