from logging import info
from turtle import position

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

    def load(self, job_name, file_tag, data:bytes, use_bar=True):
        params = {
            "tag": job_name,
            "filename": file_tag,
        }
        e = MultipartEncoder(fields=fields)
        if use_bar:
            bar = tqdm(
                desc=f"Executing loading job {job_name}",
                total=len(data),
                unit="B",
                unit_scale=True,
                unit_divisor=1024,
                leave=False
            ) 
            m = MultipartEncoderMonitor(
                e, lambda monitor: bar.update(monitor.bytes_read - bar.n)
            )
        else:
            m = e       
        fields = dict()
        fields["file"] = ("filename", data)
        r = self.conn._req("POST", self.conn.restppUrl + "/ddl/" + self.conn.graphname, params=params, data=m)
        bar.close()
        return r


    def load_bigquery(self, kind, bs, maxrows, test, jobname, filetag, bq_arg):
        import csv
        from data.bigquery import DataSource
        bigquery = DataSource()
        
        if test:
            bigquery.test_import_data(kind, bq_arg, bs, maxrows)
        else:
            imported_data = bigquery.import_data(kind, bq_arg, bs, maxrows)
            params = {
                "tag": jobname,
                "filename": filetag,
            }
            results = dict()
            for i, df in enumerate(imported_data):
                with begin(f"Fetching batch {i + 1} of {int(maxrows / bs)}") as op:
                    data = df.to_csv(index=False, sep=',', header=True, quoting=csv.QUOTE_MINIMAL).encode('utf-8')
                    op.complete()
                upload_data_bar = tqdm(
                    desc=f"Uploaing batch {i + 1} to TigerGraph server",
                    unit="B",
                    unit_scale=True,
                    unit_divisor=1024,
                    total=len(data),
                    leave=True,
                )
                fields = dict()
                fields["file"] = ("filename", data)
                e = MultipartEncoder(fields=fields)
                m = MultipartEncoderMonitor(
                    e, lambda monitor: upload_data_bar.update(monitor.bytes_read - upload_data_bar.n)
                )
                results[i] = self.conn._req("POST", self.conn.restppUrl + "/ddl/" + self.conn.graphname, params=params, data=m)
                upload_data_bar.close()
            return results
                
            
