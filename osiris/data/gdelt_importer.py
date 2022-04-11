import gdelt

from base.runtime import serialize_to_json
from base.timer import begin
from core.importer import DataImporter

class DataImporter(DataImporter):
    """Import data from Reddit."""

    def __init__(self, table, tg_user, tg_pass):
        self.table = table
        self.tg_user = tg_user
        self.tg_pass = tg_pass
        self.gd2 = gdelt.gdelt(version=2)

    def get_importer_info(self):
        pass
    
    def import_data(self, *args):
        """Import Reddit data using the parameters specified"""
        results = self.gd2.Search('2016 Nov 1',table='mentions',output='json')
        return results
        
  
        


