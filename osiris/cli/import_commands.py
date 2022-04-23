import csv
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
@click.option('--google-app-creds', envvar="GOOGLE_APPLICATION_CREDENTIALS")
@click.option('--query', 'kind', flag_value='query',  help='Retrieve data using a BigQuery query')
@click.option('--table', 'kind', flag_value='table', default=True, help='Retrieve data from a BigQuery table')
@click.option('--bs', type=int, default=1000, help='The batch-size to use when retrieving data from the table.')
@click.option('--limit', type=int, default=None)
@click.argument('bq-arg')
@click.argument('filename', type=click.Path())
def import_bigquery(google_app_creds, kind, bs, limit, bq_arg, filename):
   from data import bigquery
   bigquery = bigquery.DataSource()
   rows_iter = bigquery.import_data(kind, bq_arg, bs)
   with begin(f'Writing data to CSV file {filename}') as op:
      batch_count = 0
      total_rows = 0
      for rows in rows_iter:
         with begin(f'Fetching batch {batch_count + 1} of {bs} rows from BigQuery') as bop:
            df:pd.DataFrame = rows.to_dataframe()
            batch_count = batch_count + 1
            total_rows = total_rows + rows.num_results
            info(f'Number of rows in batch {batch_count}: {rows.num_results}.')
            print(df.info())
            info(f'Total rows: {total_rows}')
            batch_count = batch_count + 1
            bop.complete()
         if total_rows >= limit:
            break
      op.complete()

  # with begin(f'Writing data to CSV file {filename}') as op:

      #df.iloc[5000:10000].to_csv('2' + filename, index=False, quoting=csv.QUOTE_NONNUMERIC)
      #op.complete()

