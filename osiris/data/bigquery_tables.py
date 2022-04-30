"""Helpers to get tabular GDELT data from Google BigQuery"""
from datetime import datetime

import pandas as pd

from osiris_global import tqdm_iter
from data.bigquery import DataSource

bigquery = DataSource()

def events(start_date:datetime, bs=10000, maxrows=None):
    table:str = ''
    if start_date >= '2022-01-01':
        table = 'osiris-347701.gdelt_snapshots.events_actions_20220000_20220421'
    elif start_date >= '2020-04-01':
        table = 'osiris-347701.gdelt_snapshots.events_actions_20200400_'
    else:
        raise "An events table snapshot doesn't exist for this date range"

    data = bigquery.import_data("table", table, bs, maxrows)
    return pd.concat(tqdm_iter(data, desc=f'Fetch events table data', total = (int (maxrows / bs) if maxrows is not None else None), unit="batch"))

def actors(start_date:datetime, bs=10000, maxrows=None):
    table:str = ''
    if start_date >= '2022-01-01':
        table = 'osiris-347701.gdelt_snapshots.events_actors_20220000_'
    elif start_date >= '2020-04-01':
        table = 'osiris-347701.gdelt_snapshots.events_actors_20200400_'
    else:
        raise "An actors table snapshot doesn't exist for this date range"
    
    data = bigquery.import_data("table", table, bs, maxrows)
    return pd.concat(tqdm_iter(data, desc=f'Fetch event actors table data', total = (int (maxrows / bs) if maxrows is not None else None), unit="batch"))

def mentions(start_date:datetime, bs=10000, maxrows=None):
    table:str = ''
    if start_date >= '2022-01-01':
        table = 'osiris-347701.gdelt_snapshots.events_mentions_20220400_'
    elif start_date >= '2020-04-01':
        table = 'osiris-347701.gdelt_snapshots.events_mentions_2020040000_'
    else:
        raise "A mentions table snapshot doesn't exist for this date range"
    
    data = bigquery.import_data("table", table, bs, maxrows)
    return pd.concat(tqdm_iter(data, desc=f'Fetch event mentions table data', total = (int (maxrows / bs) if maxrows is not None else None), unit="batch"))