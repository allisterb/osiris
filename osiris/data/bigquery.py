from logging import info, error, debug
         
from google.cloud import bigquery

from bq_iterate.src.bq_iterate.core import BqTableRowsIterator, BqQueryRowsIterator, bq_iterator

from base.timer import begin
from core.datasource import DataSource

class DataSource(DataSource):
    """Import and monitor data from Google BigQuery"""

    def __init__(self):
        super().__init__("Google BigQuery")
        self.bqclient = bigquery.Client()
   
    def get_info(self):
        pass
    
    def import_data_table(self, bqtable, bs):
        with begin(f'Retrieving rows iterator from BigQuery table {bqtable}') as op:
            #self.bqclient.list_rows(bqtable).
            it = bq_iterator(BqTableRowsIterator(self.bqclient, bqtable, bs))
            op.complete()
            return it 

    def import_data_query(self, bqquery, bs):
        with begin(f'Retrieving rows iterator for BigQuery query') as op:
            it = bq_iterator(BqQueryRowsIterator(self.bqclient, bqquery, bs))
            op.complete()
            return it

    def import_data(self, query_type, *args):
        if query_type == 'table':
            return self.import_data_table(args[0], args[1])
        elif query_type == 'query':
            return self.import_data_query(args[0], args[1])
        else:
            raise "Unsupported BigQuery import type."
