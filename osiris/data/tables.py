"""Get shaped data"""
from datetime import datetime
from tqdm import tqdm

from tqdm.auto import trange
import pandas as pd

import osiris_global
from osiris_global import tqdm_iter
from base.timer import begin
from data.bigquery import DataSource

bigquery = DataSource()

def events(start_date:datetime, end_date:datetime=None, bs=10000, maxrows=None):
    table:str = ''
    if start_date >= '20022-01-01':
        table = "osiris-347701.gdelt_snapshots.events_actions_20220000_20220421"
    data = bigquery.import_data("table", table, bs, maxrows)
    return pd.concat(tqdm_iter(data, desc=f'Fetch events data in batches of {bs} rows', total = (int (maxrows / bs) if maxrows is not None else None), unit="batch"))



