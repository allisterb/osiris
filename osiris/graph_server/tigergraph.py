from base.timer import begin

import pyTigerGraph as tg

from core.graph_server import GraphServer

class GraphServer(GraphServer):
    """A TigerGraph graph database server"""

    def __init__(self, host, graph_name, user = None, passwd = None, token = None):
        super().__init__("TigerGraph", host, graph_name, user, passwd, token)
        self.host = host
        self.graph_name = graph_name
        self.user = user
        self.passwd = passwd
        self.token = token
        if self.token is not None and self.passwd is None:
            self.conn = tg.TigerGraphConnection(host=self.host, graphname=self.graph_name, apiToken=self.token)
        else:
            assert self.user is not None
            assert self.passwd is not None
            self.conn = tg.TigerGraphConnection(host=self.host, graphname=self.graph_name, username=self.user, password=self.passwd)
            
    def get_info(self):
        info = dict()
        e = self.conn.getEndpoints()
        p = self.conn._get(
            self.conn.restppUrl + "/showprocesslist/" + self.graph_name, resKey=None)
        info['endpoints'] = e
        info['process list'] = p['results']
        return info

    def get_token(self, api_secret=''):
        return self.conn.getToken(api_secret)

    def get_statistics(self, seconds=59):
        return self.conn.getStatistics(seconds)

    def query(self, q):
        with begin(f'Executing query on graph {self.graph_name}') as op:
            r = self.conn.gsql(q)
            op.complete()
            return r
        