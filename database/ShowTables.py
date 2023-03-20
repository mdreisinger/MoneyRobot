"""
Code to show data in tables.
"""

import click
from tabulate import tabulate

from .DatabaseConnection import get_connection

@click.command()
def show_tables():
    """
    This function shows the data in all tables in our RDS instance.
    The database information it uses can be defined in environment variables:
    RDS_HOST, USERNAME, PASSWORD, DB_NAME.
    If these environment variables are not defined, it will use the information
    defined in 'moneyrobot-dev-secret' in SecretsManager.
    """
    conn = get_connection()
    columns = ("transaction_id, transaction_date, transactor, transaction_category,"
               " items, transaction_amount, time_modified")
    with conn.cursor() as cur:
        try:
            cur.execute(f"select {columns} from transactions"
                        " ORDER BY transaction_date")
        except Exception as error:
            print(f"Error printing tables: {error}")
            return
        table = cur.fetchall()
        headers = [column.strip() for column in columns.split(",")]
        print("\ntransactions:")
        print(tabulate(table,
                       headers=headers,
                       tablefmt='mysql'))
        print("\n")
