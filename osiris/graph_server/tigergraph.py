from pathlib import Path

import pyTigerGraph as tg
from tqdm.auto import tqdm, trange
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

from base.timer import begin
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

    def create_secret(self, alias):
        return self.conn.createSecret(alias)

    def get_token(self, api_secret=''):
        return self.conn.getToken(api_secret)

    def get_statistics(self, seconds=59):
        return self.conn.getStatistics(seconds)
        
    def query(self, q):
        with begin(f'Executing query on graph {self.graph_name}') as op:
            r = self.conn.gsql(q)
            op.complete()
            return r

    def load(self, job_name, file_tag, data:bytes, bar:tqdm=None):
        params = {
            "tag": job_name,
            "filename": file_tag,
        }
        if bar == None:
            bar = tqdm(
                desc=f"Executing loading job {job_name}",
                total=len(data),
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                leave=False
            )        
        fields = dict()
        fields["file"] = ("filename", data)
        e = MultipartEncoder(fields=fields)
        m = MultipartEncoderMonitor(
            e, lambda monitor: bar.update(monitor.bytes_read - bar.n)
        )
        r = self.conn._req("POST", self.conn.restppUrl + "/ddl/" + self.conn.graphname, params=params, data=m)
        bar.close()
        return r