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
        self.conn = tg.TigerGraphConnection(host=self.host, graphname=self.graph_name, username=self.user, password=self.passwd, apiToken=self.token)
            
    def echo(self):
        return self.conn.echo()

    def get_info(self):
        info = dict()
        e = self.conn.getEndpoints()
        p = self.conn._get(
            self.conn.restppUrl + "/showprocesslist/" + self.graph_name, resKey=None)
        info['endpoints'] = self.conn.getEndpoints(True, True)
        info['edges'] = self.conn.getEdgeStats("*")
        info['vertices'] = self.conn.getVertexStats("*")
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

    def load(self, job_name, file_tag, file_path):
        with begin(f'Executing loading job {job_name} with file {file_path}') as op:
            r = self.conn.uploadFile(jobName=job_name, filePath=file_path, fileTag=file_tag)
            op.complete()
            return r