from logging import info

import click

from cli.commands import data_import
from cli.util import *

@data_import.command('gdelt')
@click.argument('table')
@click.argument('target', default='tigergraph')
@click.option('--user', envvar='OSIRIS_GRAPH_SERVER_USER', default = None)
@click.option('--passwd', envvar='OSIRIS_GRAPH_SERVER_PASS', default = None)
@click.option('--token', envvar='OSIRIS_GRAPH_SERVER_TOKEN', default = None)
def import_gdelt(table, target, user, passwd, token):
   from data.gdelt_importer import DataImporter
   info(table)
   info(target)
   info(user)
   info(passwd)
   info(token)
   importer = DataImporter(table, user, passwd)
   importer.import_data()

   
