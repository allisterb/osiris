import click

from cli.commands import data_import
from cli.util import *

@data_import.command('gdelt')
@click.argument('table')
@click.argument('target')
@click.option('--user', envvar='OSIRIS_GRAPH_SERVER_USER', default = None)
@click.option('--passwd', envvar='OSIRIS_GRAPH_SERVER_PASS', default = None)
@click.option('--token', envvar='OSIRIS_GRAPH_SERVER_TOKEN', default = None)
def import_gdelt(table, target, user, passwd, token):
   from data.gdelt_importer import DataImporter
   
