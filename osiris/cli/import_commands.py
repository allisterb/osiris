import csv
from logging import info, error

import pandas as pd
import click
from rich import print

from base.timer import begin
from cli.commands import data_import
from cli.util import *

@data_import.command('gdelt', help='Import data from the GDELT file server into a graph database server.')
@click.argument('table')
@click.argument('start-date')
@click.argument('end-date')
@click.argument('filename', type=click.Path())
@click.argument('target', default='csv')
def import_gdelt(table, start_date, end_date, filename, target):
   from data.gdelt import DataSource
   gdelt = DataSource()
   df:pd.DataFrame = gdelt.import_data(table, start_date, end_date)
   with begin(f'Writing data to CSV file {filename}') as op:
      df.to_csv(filename, index=False, quoting=csv.QUOTE_NONNUMERIC)
      op.complete()

@data_import.command('bigquery', help='Import GDELTdata from a Google BigQuery table into a graph database server.')
@click.option('--google-app-creds', envvar="GOOGLE_APPLICATION_CREDENTIALS")
@click.option('--query', 'kind', flag_value='query',  help='Retrieve data using a BigQuery query')
@click.option('--table', 'kind', flag_value='table', default=True, help='Retrieve data from a BigQuery table')
@click.option('--limit', type=int, default=None)
@click.argument('bq-arg')
@click.argument('filename', type=click.Path())
def import_bigquery(google_app_creds, kind, limit, bq_arg, filename):
   from data import bigquery
   from bq_iterate import BqQueryRowIterator, batchify_iterator
   bigquery = bigquery.DataSource()
   rows = bigquery.import_data(kind, bq_arg, limit)
   
   with begin(f'Writing data to CSV file {filename}') as op:
      #df.iloc[0:500000].to_csv('1' + filename, index=False, quoting=csv.QUOTE_NONNUMERIC)
      #df.iloc[500000:1500000].to_csv('2' + filename, index=False, quoting=csv.QUOTE_NONNUMERIC)
      #df.iloc[0:5000].to_csv('1' + filename, index=False, quoting=csv.QUOTE_NONNUMERIC)
      gg =  (pd.DataFrame(rows[:10000]))
      op.complete()

  # with begin(f'Writing data to CSV file {filename}') as op:

      #df.iloc[5000:10000].to_csv('2' + filename, index=False, quoting=csv.QUOTE_NONNUMERIC)
      #op.complete()

