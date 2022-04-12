import queue
from datetime import datetime, timedelta
from logging import info, error, debug

import gdelt
import pandas as pd           

from base.timer import begin
from core.datasource import DataSource

class DataSource(DataSource):
    """Import and monitor data from GDELT"""

    def __init__(self):
        super().__init__("GDELT")
        self.gd2 = gdelt.gdelt(version=2)

    def get_info(self):
        pass
    
    def import_data(self, table, start_date, end_date):
        """Import GDELT data for a date range"""

        try:
            start_date = datetime.strptime(start_date, '%b-%d-%Y')
            end_date = datetime.strptime(end_date, '%b-%d-%Y')
        except ValueError as ve:
            error(f'A date was not in the correct format: {ve}')
            return None
        d = end_date - start_date
        days = [start_date + timedelta(days=x) for x in range((d).days + 1)]
        results:list[pd.DataFrame] = list()
        with begin(f"Import GDELT {table} for {len(days)} days from {start_date} to {end_date}") as op:
            for day in days:
                with begin(f"Import GDELT {table} for {day.strftime('%m-%d-%Y')}") as op2:
                    r = (self.gd2.Search(day.strftime('%m-%d-%Y %H:%M:%S'), coverage = True, table=table))
                    results.append(r)
                    op2.complete()
            op.complete()
        return pd.concat(results)
        
    def monitor(message_queue:queue.Queue):
        return ''