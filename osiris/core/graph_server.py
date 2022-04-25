import abc

target = None
url = None
graph_name = None
user = None
passwd = None
token = None

class GraphServer(abc.ABC):
    """A graph database server."""

    def __init__(self, name, url, graph_name, *args):
        self.name = name
        self.url = url
        self.graph_name = graph_name
        self.args = args

    @abc.abstractmethod
    def echo(self):
        """Make a basic query on a graph database server."""

    @abc.abstractmethod
    def get_info(self):
        """Get information on graph database server."""

    @abc.abstractmethod
    def create_secret(self, *args):
        """Create an API secret to use to access graph database server."""

    @abc.abstractmethod
    def get_token(self, api_secret=''):
        """Get an authentication token to access graph database server."""
        
    @abc.abstractmethod
    def get_statistics(self, seconds=59):
        """Get statistics for the last n seconds."""

    @abc.abstractmethod
    def query(self, str):
        """Run a query on the graph server."""

    @abc.abstractmethod
    def load(self, job_name, file_tag, data:bytes, *args):
        """Bulk load data to the graph_server."""

# Instance of a GraphServer.
i: GraphServer = None