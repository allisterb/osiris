import abc

class DataImporter(abc.ABC):
    """Import data."""

    def __init__(self, args=[]):
        self.args = args

    @abc.abstractmethod
    def get_importer_info(self):
        """Get information on importer"""
    
    @abc.abstractmethod
    def import_data(*args):
        """Import data using the parameters specified"""