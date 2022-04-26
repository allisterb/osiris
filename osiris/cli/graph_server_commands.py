import time
from logging import info, error

import click
from rich import print
from base.timer import begin

import osiris_global
from cli.commands import graph_server as graph_server_cmd
from cli.util import *

@graph_server_cmd.command('create-secret', help = 'Create an API secret for a graph server.')
@click.argument('alias')
@click.pass_context
def get_token(ctx:click.Context, alias):
    from core.graph_server import i as graph_server
    print(graph_server.create_secret(alias))

@graph_server_cmd.command('get-token', help = 'Get an authentication token for a graph server.')
@click.argument('secret', envvar='OSIRIS_GRAPH_SERVER_SECRET')
@click.pass_context
def get_token(ctx:click.Context, secret):
    from core.graph_server import i as graph_server
    print(graph_server.get_token(secret))

@graph_server_cmd.command('ping', help = 'Verify connectivity to a graph server instance.')
@click.pass_context
def ping(ctx:click.Context):
    from core.graph_server import i as graph_server
    with begin('Testing connectivity to REST++ API') as op:
        graph_server.get_statistics(1)
        op.complete()
    with begin('Testing connectivity to GSQL') as op:
        print(graph_server.echo())
        op.complete()

@graph_server_cmd.command('info', help = 'Print info on graph server objects and endpoints.')
@click.pass_context
def info_cmd(ctx:click.Context):
    from core.graph_server import i as graph_server
    info('Printing info for graph {graph_server.graph_name} on server {graph_server.url}')
    print(graph_server.get_info())

@graph_server_cmd.command('stats', help = 'Print graph server statistics')
@click.argument('seconds', default=59)
@click.pass_context
def statistics(ctx:click.Context, seconds):
    from core.graph_server import i as graph_server
    info(f'Printing statistics for graph {graph_server.graph_name} on server {graph_server.url} for the past {seconds} seconds...')
    print(graph_server.get_statistics(seconds))

@graph_server_cmd.command('monitor', help = 'Start a daemon process to monitor a graph server.')
@click.argument('interval', default=15)
@click.argument('report', default=59)
@click.pass_context
def monitor(_:click.Context, interval, report):
    from core.graph_server import i as graph_server
    orig_time = time.time()
    info(f'Printing statistics for graph {graph_server.graph_name} on server {graph_server.url} for the past {report} seconds...')
    print(graph_server.get_statistics(report))
    info(f'Monitoring graph {graph_server.graph_name} on server {graph_server.url} every {interval} seconds started at {time.strftime("%b-%d-%Y %H:%M:%S", time.localtime(orig_time))}...')
    last_ping_time = orig_time
    osiris_global.DAEMON = True
    while not osiris_global.KBINPUT:
        time.sleep(3)
        current_time = time.time()
        if current_time - last_ping_time >= interval:
            stats = graph_server.get_statistics(report)
            info(f'Printing statistics for graph {graph_server.graph_name} on server {graph_server.url} for the past {report} seconds...')
            print(stats)
            info(f'Monitoring graph {graph_server.graph_name} on server {graph_server.url} every {interval} seconds started at {time.strftime("%b-%d-%Y %H:%M:%S", time.localtime(orig_time))}...')
            last_ping_time = current_time

    info('osiris monitor daemon stopped.')

@graph_server_cmd.command('query', help = 'Execute a GSQL query on the graph server.')
@click.option('--text', default=None, help='Use this as the query text.')
@click.option('--file', type=click.Path(exists=True), default=None, help='Use the text in this file as the query text.')
@click.pass_context
def query_graph(_:click.Context, text, file):
    if text is None and file is None:
        exit_with_error('You must specify either the query text using --text or --file.')
    from core.graph_server import i as graph_server
    if text is not None:
        print(graph_server.query(text))
    else:
        info(f'Using file {file} as query source.')
        with open(file, 'r') as f:
            print(graph_server.query(f.read()))

@graph_server_cmd.group('load', help  = 'Load data into graph server using a loading job.')
def load_cmd(): pass

@load_cmd.command('file', help = 'Load data into graph server from a local file.')
@click.argument('jobname')
@click.argument('filetag')
@click.argument('filepath', type=click.Path(exists=True))
@click.pass_context
def load_file(_:click.Context, jobname, filetag, filepath):
    from core.graph_server import i as graph_server
    print(graph_server.load_file(jobname, filetag, filepath))

@load_cmd.command('bigquery', help = 'Load data into graph server using Google BigQuery.')
@click.option('--google-app-creds', required=True, envvar="GOOGLE_APPLICATION_CREDENTIALS")
@click.option('--query', 'kind', flag_value='query',  help='Retrieve data using a BigQuery query')
@click.option('--table', 'kind', flag_value='table', default=True, help='Retrieve data from a BigQuery table')
@click.option('--bs', type=int, default=1000, help='The batch-size to use when retrieving data from the table.')
@click.option('--maxrows', type=int, default=None)
@click.option('--test', is_flag=True, default=False, help='Only get the first batch of results and print information on them.')
@click.argument('jobname')
@click.argument('filetag')
@click.argument('bq-arg')
@click.pass_context
def load_bigquery(_:click.Context, google_app_creds, kind, bs, maxrows, test, jobname, filetag, bq_arg):
    from core.graph_server import i as graph_server   
    from data.bigquery import DataSource
    bigquery = DataSource()
    if test:
        bigquery.test_import_data(kind, bq_arg, bs, maxrows)
    else:
        r = graph_server.load_bigquery(kind, bs, maxrows, test, jobname, filetag, bq_arg)
        print(r)


        
