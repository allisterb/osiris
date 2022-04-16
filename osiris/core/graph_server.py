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

    def __init__(self, name, url, graph_name, *args):
        self.name = name
        self.url = url
        self.graph_name = graph_name
        self.args = args

    @abc.abstractmethod
    def get_info(self):
        """Get information on graph database server"""

    @abc.abstractmethod
    def get_token(self, api_secret=''):
        """Get an authentication token to use with graph database server"""
        
    @abc.abstractmethod
    def get_statistics(self, seconds):
        """Get statistics for the last n seconds"""
# Instance of a GraphServer.
i: GraphServer = None