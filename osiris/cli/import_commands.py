from logging import info, error

import pandas as pd
import click
from rich import print

from cli.commands import data_import
from cli.util import *

@data_import.command('gdelt', help='Import data from GDELT into a graph database server.')
@click.argument('table')
@click.argument('start-date')
@click.argument('end-date')
@click.argument('target', default='tg')
def import_gdelt(table, start_date, end_date, target):
   from data.gdelt import DataSource
   gdelt = DataSource()
   data:pd.DataFrame = gdelt.import_data(table, start_date, end_date)
   data.info()
   print(data.head())


   
