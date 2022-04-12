from logging import info, error

import pandas as pd
import click

from cli.commands import data_import
from cli.util import *

@data_import.command('gdelt', help='Import data from GDELT into a graph database server.')
@click.argument('table')
@click.argument('start-date')
@click.argument('end-date')
@click.argument('target', default='tigergraph')
@click.option('--user', envvar='OSIRIS_GRAPH_SERVER_USER', default = None)
@click.option('--passwd', envvar='OSIRIS_GRAPH_SERVER_PASS', default = None)
@click.option('--token', envvar='OSIRIS_GRAPH_SERVER_TOKEN', default = None)
def import_gdelt(table, start_date, end_date, target, user, passwd, token):
   from data.gdelt_importer import DataImporter
   importer = DataImporter()
   data:pd.Series = importer.import_data(table, start_date, end_date)
   data.info


   
