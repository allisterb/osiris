from logging import info, error, debug

import pandas as pd           
from google.cloud import bigquery

from base.timer import begin
from core.datasource import DataSource

class DataSource(DataSource):
    """Import and monitor data from Google BigQuery"""

    def __init__(self):
        super().__init__("Google BigQuery")
        self.bqclient = bigquery.Client()
   
    def get_info(self):
        pass
    
    def import_data_table(self, bq_table, limit=None, page_size=1000):
        with begin(f'Retrieving row iterator from BigQuery table {bq_table}') as op:
            table = bigquery.TableReference.from_string(bq_table)
            rows = self.bqclient.list_rows(table, max_results=limit)
            #df = rows.to_dataframe(create_bqstorage_client=True)
            op.complete()
            return rows 

    def import_data_query(self, query_text):
        with begin(f'Retrieving row iterator for BigQuery query') as op:
            rows = self.bqclient.query(query_text).result()
            op.complete()
            return rows

    def import_data(self, query_type, *args):
        if query_type == 'table':
            return self.import_data_table(args[0], args[1])
        elif query_type == 'query':
            return self.import_data_query(args[0])
        else:
            raise "Unsupported BigQuery import type."
