from distutils.log import error
from logging import info

import pyTigerGraph as tg
from tqdm.auto import tqdm, trange
from requests_toolbelt import MultipartEncoder, MultipartEncoderMonitor

import osiris_global
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

    def get_info(self, vertex_type='*', edge_type='*'):
        info = dict()
        try:
            info['vertices'] = self.conn.getVertexStats(vertex_type)
        except Exception as e:
            error(f'Error fetching node stats: {e}.')
        try:
            info['edges'] = self.conn.getEdgeStats(edge_type)
        except Exception as e:
            error(f'Error fetching edge stats: {e}.')
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
        fields = dict()
        fields["file"] = ("filename", data)
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
        r = self.conn._req("POST", self.conn.restppUrl + "/ddl/" + self.conn.graphname, params=params, data=m)
        bar.close()
        return r


    def load_bigquery(self, kind, bs, maxrows, skip_batches, test, jobname, filetag, bq_arg):
        import csv
        from data.bigquery import DataSource
        bigquery = DataSource()
        if test:
            bigquery.test_import_data(kind, bq_arg, bs, maxrows)
        else:
            with begin(f'Load data from Google BigQuery {kind} {bq_arg} in batches of {bs} rows') as lop:
                imported_data = bigquery.import_data(kind, bq_arg, bs, maxrows)
                params = {
                    "tag": jobname,
                    "filename": filetag,
                }
                headers={"RESPONSE-LIMIT": str(524288000)}
                results = dict()
                for i, df in enumerate(imported_data):
                    if osiris_global.KBINPUT:
                        lop.abandon()
                        return results
                    if i < skip_batches:
                        info(f'Skipping batch {i}...')
                        continue
                    with begin(f"Fetching batch {i + 1} of {int(maxrows / bs)}") as op:
                        data = df.to_csv(index=False, sep=',', header=True, quoting=csv.QUOTE_MINIMAL).encode('utf-8')
                        op.complete()
                    with begin(f"Uploading batch {i + 1} of {int(maxrows / bs)}") as op:
                        upload_data_bar = tqdm(
                            desc=f"Uploading batch {i + 1} to TigerGraph server",
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
                        results[i] = self.conn._req("POST", self.conn.restppUrl + "/ddl/" + self.conn.graphname, params=params, headers=headers, data=m)
                        upload_data_bar.close()
                        op.complete()
                lop.complete()
                return results

    def gsqlquery(self):
        import requests
        from requests.auth import HTTPBasicAuth
        res = requests.get(self.conn.gsUrl + "/gsqlserver/interpreted_query", verify=False, auth=HTTPBasicAuth(self.user, self.passwd))
