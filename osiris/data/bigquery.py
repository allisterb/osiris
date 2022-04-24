from logging import info, error, debug
         
from google.cloud import bigquery
from google.cloud.bigquery.table import RowIterator
from google.cloud.bigquery import _tqdm_helpers, _pandas_helpers
from google.cloud.bigquery_storage import BigQueryReadClient
import pyarrow
import pandas as pd
from pyparsing import RecursiveGrammarException

from bq_iterate.src.bq_iterate.core import BqTableRowsIterator, BqQueryRowsIterator, bq_iterator

from base.timer import begin
from core.datasource import DataSource

class DataSource(DataSource):
    """Import and monitor data from Google BigQuery"""

    def __init__(self):
        super().__init__("Google BigQuery")
        self.bqclient = bigquery.Client()
        self.bqstorageclient = BigQueryReadClient()
   
    def get_info(self):
        pass
    
    def import_data_table(self, bqtable, bs):
        return bq_iterator(BqTableRowsIterator(self.bqclient, bqtable, bs))
            
    def import_data_query(self, bqquery, bs):
        return bq_iterator(BqQueryRowsIterator(self.bqclient, bqquery, bs))
            
    def import_data(self, query_type, *args):
        bs = args[1]
        max_rows = args[2]
        rows_iter:RowIterator = None
        if query_type == 'table':
            rows_iter = self.import_data_table(args[0], args[1])
        elif query_type == 'query':
            rows_iter = self.import_data_query(args[0], args[1])
        else:
            raise "Unsupported BigQuery import type."
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
                yield df
            if max_rows is not None and total_rows >= max_rows:
                break

    @staticmethod
    def rows_to_arrow(
        rows:RowIterator,
        bqstorage_client: BigQueryReadClient,
        progress_bar_type: str = None,
    ) -> "pyarrow.Table":
        try:
            progress_bar = _tqdm_helpers.get_progress_bar(
                progress_bar_type, "Downloading", rows.total_rows, "rows"
            )
            record_batches = []
            for record_batch in rows.to_arrow_iterable(
                bqstorage_client=bqstorage_client
            ):
                record_batches.append(record_batch)
                if progress_bar is not None:
                    # In some cases, the number of total rows is not populated
                    # until the first page of rows is fetched. Update the
                    # progress bar's total to keep an accurate count.
                    progress_bar.total = progress_bar.total or rows.total_rows
                    progress_bar.update(record_batch.num_rows)
            if progress_bar is not None:
                # Indicate that the download has finished.
                progress_bar.close()
        finally:
            #bqstorage_client._transport.grpc_channel.close()  # type: ignore
            return pyarrow.Table.from_batches(record_batches)

    @staticmethod
    def rows_to_df(rows:RowIterator, bqstorage_client: BigQueryReadClient, progress_bar_type:str):
        record_batch = bigquery.to_arrow(
            rows,
            bqstorage_client=bqstorage_client,
            progress_bar_type=progress_bar_type,
        )

        date_as_object = not all(
            rows.__can_cast_timestamp_ns(col)
            for col in record_batch
            # Type can be date32 or date64 (plus units).
            # See: https://arrow.apache.org/docs/python/api/datatypes.html
            if str(col.type).startswith("date")
        )

        timestamp_as_object = not all(
            rows.__can_cast_timestamp_ns(col)
            for col in record_batch
            # Type can be timestamp (plus units and time zone).
            # See: https://arrow.apache.org/docs/python/api/datatypes.html
            if str(col.type).startswith("timestamp")
        )

        if len(record_batch) > 0:
            df = record_batch.to_pandas(
                date_as_object=date_as_object,
                timestamp_as_object=timestamp_as_object,
                integer_object_nulls=True,
                types_mapper=_pandas_helpers.default_types_mapper(
                    date_as_object=date_as_object
                ),
            )
        else:
            df = pd.DataFrame([], columns=record_batch.schema.names)
        return df



