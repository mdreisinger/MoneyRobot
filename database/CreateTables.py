"""
Code to create tables in moneyrobot db given sql file.
"""
import pathlib

import click

from .DatabaseConnection import get_connection


@click.command()
def create_tables():
    """
    This function creates new tables in our RDS instance.
    The database information it uses can be defined in environment variables:
    RDS_HOST, USERNAME, PASSWORD, DB_NAME.
    If these environment variables are not defined, it will use the information
    defined in 'moneyrobot-dev-secret' in SecretsManager.
    """
    conn = get_connection()

    cur_dir = pathlib.Path(__file__).parent.resolve()

    with open(f'{cur_dir}/create_tables.sql', 'r', encoding='utf-8') as sql_file:
        sql_commands = sql_file.read().split(";")

    with conn.cursor() as cur:
        for command in sql_commands:
            if command:
                try:
                    print(f"Executing command:\n {command}\n\n")
                    cur.execute(command)
                    conn.commit()
                except Exception as error:
                    print(f"Failed to execute command. Error: {error}")

        cur.execute("show tables")
        print("The following tables have been added to the database:")
        for row in cur:
            print(row[0])
    conn.commit()
