import abc
from tkinter.messagebox import NO

target = None
url = None
graph_name = None
user = None
passwd = None
token = None

class GraphServer(abc.ABC):
    """A graph database server."""

    def __init__(self, name, *args):
        self.name = name
        self.args = args

    @abc.abstractmethod
    def get_info(self):
        """Get information on graph database server"""

    @abc.abstractmethod
    def get_token(self, api_secret=''):
        """Get an authentication token to use with graph database server"""

# Instance of a GraphServer.
i: GraphServer = None