import csv
from logging import info, debug
         
from google.cloud import bigquery
from google.cloud.bigquery_storage import BigQueryReadClient

import pandas as pd
from rich import print

from bq_iterate.src.bq_iterate.core import BqTableRowsIterator, BqQueryRowsIterator, bq_iterator
from core.datasource import DataSource

class DataSource(DataSource):
    """Import and monitor data from Google BigQuery"""

    def __init__(self):
        super().__init__("Google BigQuery")
        self.bqclient = bigquery.Client()
        self.bqstorageclient = BigQueryReadClient()
        self.total_rows = 0
   
    def get_info(self):
        pass
    
    def import_data_table(self, bqtable, bs):
        self.total_rows = self.bqclient.list_rows(bqtable).total_rows
        return bq_iterator(BqTableRowsIterator(self.bqclient, bqtable, bs))
            
    def import_data_query(self, bqquery, bs):
        self.total_rows = self.bqclient.list_rows(self.bqclient.query(bqquery).destination).total_rows
        return bq_iterator(BqQueryRowsIterator(self.bqclient, bqquery, bs))
            
    def import_data(self, query_type, *args):
        bs = args[1]
        max_rows = args[2]
        rows_iter:iter["RowIterator"] = None
        if query_type == 'table':
            rows_iter = self.import_data_table(args[0], bs)
        elif query_type == 'query':
            rows_iter = self.import_data_query(args[0], bs)
        else:
            raise "Unsupported BigQuery import type."
        if max_rows < self.total_rows:
            self.total_rows = max_rows
        debug(f'Total rows to fetch: {self.total_rows}.')
        batch_count = 0
        row_count = 0
        for rows in rows_iter:
            debug(f'Fetching batch {batch_count + 1} of {bs} rows from BigQuery {query_type}...')
            df:pd.DataFrame = rows.to_dataframe()
            batch_count = batch_count + 1
            row_count = row_count + rows.num_results
            debug(f'Number of rows in batch {batch_count}: {rows.num_results}.')
            debug(f'Total rows fetched: {row_count}')
            batch_count = batch_count + 1
            yield df
            if max_rows is not None and row_count >= max_rows:
                break
    
    def test_import_data(self, query_type, *args):
        imported_data:iter["pd.DataFrame"] = self.import_data(query_type, args[0], args[1], args[2])
        info(f'Test mode for import enabled.')
        df:pd.DataFrame = next(imported_data)
        print(df)
        data_bytes = df.to_csv(index=False, sep=',', header=True, quoting=csv.QUOTE_NONNUMERIC).encode('utf-8')
        info(f'Size of CSV data batch is {len(data_bytes)} bytes.')