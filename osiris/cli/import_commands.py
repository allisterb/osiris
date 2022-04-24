import csv
from email.policy import default
from logging import info, error

import pandas as pd
import click
from rich import print
from google.cloud.bigquery.table import RowIterator
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

@data_import.command('bigquery', help='Import GDELT data from a Google BigQuery table into a graph database server.')
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
      imported_data = bigquery.import_data(kind, bq_arg, bs, maxrows)
      if test:
         info(f'Test mode for import enabled.')
         df:pd.DataFrame = next(imported_data)
         df.to_csv()
         print(df)
      else:
         for df in imported_data:
            print(df)
      op.complete()