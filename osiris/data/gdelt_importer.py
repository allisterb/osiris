import queue
from datetime import datetime, timedelta
from logging import info, error, debug

import gdelt
import pandas as pd           

from base.timer import begin
from core.importer import DataImporter

class DataImporter(DataImporter):
    """Import data from GDELT"""

    def __init__(self):
        super().__init__("GDELT")
        self.gd2 = gdelt.gdelt(version=2)

    def get_importer_info(self):
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
        results:pd.DataFrame = pd.DataFrame()
        for day in days:
            with begin(f'Import GDELT {table} for {day}') as op:
                r = (self.gd2.Search(day.strftime('%m-%d-%Y %H:%M:%S'), coverage = True, table=table))
                results.append(r)
                op.complete()
                return results
        
    def monitor(message_queue:queue.Queue):
        return ''