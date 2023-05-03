"""
Basic method to get db connection parameters.

Unfortunately copy pastad this from database dir to get around stupid import errors 
"""

import json
import os

from aws_secretsmanager_caching import SecretCache, SecretCacheConfig
import botocore


def get_db_info():
    """
    Function to get DB info from either env variables or SecretsManager.
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

    return rds_host, username, password, db_name
