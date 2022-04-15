import abc

class DataSource(abc.ABC):
    """A source for importing data into a graph database."""

    def __init__(self, name, args=[]):
        self.name = name
        self.args = args

    @abc.abstractmethod
    def get_info(self):
        """Get information on data source"""
    
    @abc.abstractmethod
    def import_data(*args):
        """Import data from data source using the parameters specified"""