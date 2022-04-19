from logging import info, error

import pandas as pd
import click
from rich import print

from cli.commands import data_import
from cli.util import *

@data_import.command('gdelt', help='Import data from the GDELT file server into a graph database server.')
@click.argument('table')
@click.argument('start-date')
@click.argument('end-date')
@click.argument('target', default='csv')
def import_gdelt(table, start_date, end_date, target):
   from data.gdelt import DataSource
   gdelt = DataSource()
   data:pd.DataFrame = gdelt.import_data(table, start_date, end_date)
   data.info()
   print(data.head())


@data_import.command('bigquery', help='Import data from a Google BigQuery table into a graph database server.')
@click.option('--google-app-creds', envvar="GOOGLE_APPLICATION_CREDENTIALS")
@click.argument('bq-table')
@click.argument('tg-table')
@click.argument('target', default='csv')
def import_bigquery(google_app_creds, bq_table, tg_table, target):
   from google.cloud import bigquery
   bqclient = bigquery.Client()
   table = bigquery.TableReference.from_string(bq_table)
   print(table.project)
   
