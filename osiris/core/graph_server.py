import abc

target = None
api_url = None
graph_name = None
user = None
passwd = None
token = None

class GraphServer(abc.ABC):
    """A graph database server."""

    def __init__(self, name, args=[]):
        self.name = name
        self.args = args

    @abc.abstractmethod
    def get_info(self):
        """Get information on graph server"""