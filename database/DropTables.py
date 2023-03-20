"""
Code to drop all tables in moneyrobot db given sql file.
"""

import click

from .DatabaseConnection import get_connection


@click.command()
def drop_tables():
    """
    This function drops all tables in our RDS instance.
    The database information it uses can be defined in environment variables:
    RDS_HOST, USERNAME, PASSWORD, DB_NAME.
    If these environment variables are not defined, it will use the information
    defined in 'moneyrobot-dev-secret' in SecretsManager.
    """
    conn = get_connection()

    with conn.cursor() as cur:
        cur.execute("show tables")
        tables = cur.fetchall()
        print(tables)
        cur.execute("SET FOREIGN_KEY_CHECKS = 0")
        for table_tuple in tables:
            print(f"Dropping table: {table_tuple[0]}")
            cur.execute(f"drop table {table_tuple[0]}")
            conn.commit()
        cur.execute("SET FOREIGN_KEY_CHECKS = 1")
    conn.commit()
