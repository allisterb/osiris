import abc

class DataImporter(abc.ABC):
    """Import data into graph database."""

    def __init__(self, name, args=[]):
        self.name = name
        self.args = args

    @abc.abstractmethod
    def get_importer_info(self):
        """Get information on data importer"""
    
    @abc.abstractmethod
    def import_data(*args):
        """Import data using the parameters specified"""