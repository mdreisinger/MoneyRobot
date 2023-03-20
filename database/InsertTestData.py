"""
Module to insert test data into the moneyrobot database.
"""

import click


@click.command()
def insert_test_data():
    """
    Function to insert test data into the moneyrobot database.
    """
    print("Insert test data called!")
