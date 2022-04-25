import csv
from logging import info, error

import pandas as pd
import click
from rich import print
from google.cloud.bigquery.table import RowIterator
from base.timer import begin
from cli.commands import data_import
from cli.util import *

@data_import.command('gdelt', help='Import data from the GDELT file server.')
@click.argument('table')
@click.argument('start-date')
@click.argument('end-date')
@click.argument('filename', type=click.Path())
def import_gdelt(table, start_date, end_date, filename):
   from data.gdelt import DataSource
   gdelt = DataSource()
   df:pd.DataFrame = gdelt.import_data(table, start_date, end_date)
   with begin(f'Writing data to CSV file {filename}') as op:
      df.to_csv(filename, index=False, quoting=csv.QUOTE_NONNUMERIC)
      op.complete()

@data_import.command('bigquery', help='Import data from a Google BigQuery table.')
@click.option('--google-app-creds', required=True, envvar="GOOGLE_APPLICATION_CREDENTIALS")
@click.option('--query', 'kind', flag_value='query',  help='Retrieve data using a BigQuery query')
@click.option('--table', 'kind', flag_value='table', default=True, help='Retrieve data from a BigQuery table')
@click.option('--bs', type=int, default=1000, help='The batch-size to use when retrieving data from the table.')
@click.option('--maxrows', type=int, default=None)
@click.option('--test', is_flag=True, default=False, help='Only get the first batch of results and print information on them.')
@click.argument('bq-arg')
@click.argument('filename', type=click.Path())
def import_bigquery(google_app_creds, kind, bs, maxrows, test, bq_arg, filename):
   from data import bigquery
   bigquery = bigquery.DataSource()
   with begin(f'Importing data from BigQuery {kind} {bq_arg} to {filename}') as op:
      if test:
         bigquery.test_import_data(kind, bq_arg, bs, maxrows)
      else:
         imported_data = bigquery.import_data(kind, bq_arg, bs, maxrows)
         for i, df in enumerate(imported_data):
            prefix = '' if i == 0 else str(i + 1) + '_'
            info(f'Writing data batch to {prefix + filename}...')
            df.to_csv(prefix + filename, index=False, sep=',', header=True, quoting=csv.QUOTE_NONNUMERIC)
      op.complete()