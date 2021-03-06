"""Example of several Dependency Injector IoC containers.

Alternative injections definition style #1.
"""

import sqlite3
import boto.s3.connection
import example.services

import dependency_injector.containers as containers
import dependency_injector.providers as providers


class Platform(containers.DeclarativeContainer):
    """IoC container of platform service providers."""

    database = providers.Singleton(sqlite3.connect) \
        .add_args(':memory:')

    s3 = providers.Singleton(boto.s3.connection.S3Connection) \
        .add_kwargs(aws_access_key_id='KEY',
                    aws_secret_access_key='SECRET')


class Services(containers.DeclarativeContainer):
    """IoC container of business service providers."""

    users = providers.Factory(example.services.Users) \
        .add_kwargs(db=Platform.database)

    auth = providers.Factory(example.services.Auth) \
        .add_kwargs(db=Platform.database,
                    token_ttl=3600)

    photos = providers.Factory(example.services.Photos) \
        .add_kwargs(db=Platform.database,
                    s3=Platform.s3)
