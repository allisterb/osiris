from core.graph_server import GraphServer, graph_api_url, graph_user, graph_passwd, graph_token

class GraphServer(GraphServer):
    """A TigerGraph graph server"""

    def __init__(self, host, graph_name, user = None, passwd = None, token = None)):
        super().__init__("GDELT")
    #self.gd2 = gdelt.gdelt(version=2)