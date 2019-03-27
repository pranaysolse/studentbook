import click
from flask import current_app, g
from flask.cli import with_appcontext
import sqlite3


def get_db():
    if 'db' not in g:
        g.db = sqlite3.connect(
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db


def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()


def init_db():
    """
    this function can initialized the database by first calling the get_db
     function to connect to database it then execute default sql
     schema to create tables for application
    """
    db = get_db()

    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))


@click.command('init-db')
@with_appcontext
def init_db_command():
    """
    clear the exiting dara and create database via cli
    """
    init_db()
    click.echo("initialized the database")


def init_app(app):
    """
    actuall initialization of database for app instance
    first function call destroy all database of last instance
    second one initializws the db
    """
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_command)