import abc

class DataSource(abc.ABC):
    """A source for importing data into graph database."""

    def __init__(self, name, args=[]):
        self.name = name
        self.args = args

    @abc.abstractmethod
    def get_info(self):
        """Get information on data importer"""
    
    @abc.abstractmethod
    def import_data(*args):
        """Import data using the parameters specified"""