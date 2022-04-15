from core.graph_server import GraphServer
import pyTigerGraph as tg

class GraphServer(GraphServer):
    """A TigerGraph graph server"""

    def __init__(self, host, graph_name, user = None, passwd = None, token = None):
        super().__init__("GDELT", host, graph_name, user, passwd, token)
        self.host = host
        self.graph_name = graph_name
        self.user = user
        self.passwd = passwd
        self.token = token
        if self.token is not None:
            self.conn = tg.TigerGraphConnection(host=self.host, graphname=self.graph_name, apiToken=self.token)
        else:
            assert self.user is not None
            assert self.passwd is not None
            self.conn = tg.TigerGraphConnection(host=self.host, graphname=self.graph_name, username=self.user, password=self.passwd)
            
    def get_info(self):
        return self.conn.getEndpoints()