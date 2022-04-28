from functools import partial
import queue
from datetime import datetime, timedelta
from logging import info, error, debug

import gdelt
import pandas as pd           

from osiris_global import tqdm_iter, tqdm_debug
from base.timer import begin
from core.datasource import DataSource

class DataSource(DataSource):
    """Import and monitor data from the GDELT file server"""

    def __init__(self):
        super().__init__("GDELT")
        self.gd2 = gdelt.gdelt(version=2)

    def get_info(self):
        pass
    
    def import_data(self, table, start_date, end_date, output='df'):
        """Import GDELT data for a date range"""
        try:
            start_date = datetime.strptime(start_date, '%b-%d-%Y %H:%M:%S')
            end_date = datetime.strptime(end_date, '%b-%d-%Y %H:%M:%S')
            return self.import_data_hours(table, start_date, end_date, output)
        except ValueError as ve:
            try:
                start_date = datetime.strptime(start_date, '%b-%d-%Y')
                end_date = datetime.strptime(end_date, '%b-%d-%Y')
                return self.import_data_days(table, start_date, end_date, output)
            except ValueError as ve:
                error(f'A date was not in the correct format: {ve}')
                return None
            
    def import_data_hours(self, table, start_date, end_date, output='df'):
        """Import GDELT data for a date range spanning multiple hours"""
        d = end_date - start_date
        hours = [start_date + timedelta(hours=x) for x in range(d.days * 24 + int(d.seconds / 3600))]
        with begin(f"Importing GDELT {table} data for {len(hours)} hour(s) from {start_date.strftime('%m-%d-%Y %H:%M:%S')} to {end_date.strftime('%m-%d-%Y %H:%M:%S')}") as op:
            r = self.gd2.Search(list(map(lambda x: x.strftime('%m-%d-%Y %H:%M:%S'), hours)), coverage = False, table=table, output=output)
            op.complete()
            return r

    def import_data_days(self, table, start_date, end_date, output='df'):
        """Import GDELT data for a date range spanning multiple days"""
        d = end_date - start_date
        days = [start_date + timedelta(days=x) for x in range(d.days + 1)]
        results:list[pd.DataFrame] = list()
        with begin(f"Importing GDELT {table} data for {len(days)} day(s) from {start_date.strftime('%m-%d-%Y')} to {end_date.strftime('%m-%d-%Y')}") as op:
            _days = tqdm_iter(days, total=len(days), unit="day", desc=f'Import GDELT {table} data')
            _debug = partial(tqdm_debug, _days)
            for day in _days:
                _debug(f"Importing GDELT {table} data for {day.strftime('%m-%d-%Y')}.")
                r = self.gd2.Search(day.strftime('%m-%d-%Y %H:%M:%S'), coverage = True, table=table, output=output)
                results.append(r)
            op.complete()
        return pd.concat(results)
    
    def test_import_data(self, query_type, *args):
        pass
    
    def monitor(message_queue:queue.Queue):
        return ''

