"""
Code to show data in tables.
"""

import json
import os
import sys

from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
import botocore
import botocore.session
import click
import pymysql
from tabulate import tabulate


@click.command()
def show_tables():
    """
    This function shows the data in all tables in our RDS instance.
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
                               connect_timeout=10)
    except pymysql.MySQLError as error:
        print("ERROR: Unexpected error: Could not connect to MySQL instance.")
        print(error)
        sys.exit()
    print("SUCCESS: Connection to RDS MySQL instance succeeded")
    show_table("expenses", "cast(expense_date as date) as date, "
               "expense, payee, expense_category, items, time_modified", conn)
    show_table("expense_notes", "note, time_created, time_modified, expense_id", conn)
    show_table("income", "cast(income_date as date) as date, "
               "payor, income, income_category, time_modified", conn)
    show_table("income_notes", "note, time_created, time_modified, income_id", conn)

def show_table(table_name, columns, conn):
    """
    Generic function to print tables
    """
    with conn.cursor() as cur:
        try:
            cur.execute(f"select {columns} from {table_name}")
        except:
            print(f"{table_name} doesn't exist")
            return
        table = cur.fetchall()
        raw_headers = [column.strip() for column in columns.split(",")]
        headers = [header if "date" not in header else "date" for header in raw_headers]
        print(f"\n{table_name}:")
        print(tabulate(table,
                       headers=headers,
                       tablefmt='mysql'))
        print("\n")
