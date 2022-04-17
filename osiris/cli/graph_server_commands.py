import time
from datetime import datetime, timedelta, date
from logging import info, error
from typing_extensions import Required

import click
from rich import print

import osiris_global
from cli.commands import graph_server as graph_server_cmd
from cli.util import *

@graph_server_cmd.command('get-token', help = 'Get an authentication token for the graph server.')
@click.argument('secret', envvar='OSIRIS_GRAPH_SERVER_SECRET')
@click.pass_context
def get_token(ctx:click.Context, secret):
    from core.graph_server import i as graph_server
    print(graph_server.get_token(secret))

@graph_server_cmd.command('info', help = 'Print info on graph server')
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
@click.argument('ping', default=10)
@click.argument('report', default=59)
@click.pass_context
def monitor(ctx:click.Context, ping, report):
    from core.graph_server import i as graph_server
    orig_time = time.time()
    info(f'Printing statistics for graph {graph_server.graph_name} on server {graph_server.url} for the past {report} seconds...')
    print(graph_server.get_statistics(report))
    info(f'Monitoring graph {graph_server.graph_name} on server {graph_server.url} every {ping} seconds started at {time.strftime("%b-%d-%Y %H:%M:%S", time.localtime(orig_time))}...')
    last_ping_time = orig_time
    osiris_global.DAEMON = True
    while not osiris_global.KBINPUT:
        time.sleep(3)
        current_time = time.time()
        if current_time - last_ping_time >= ping:
            stats = graph_server.get_statistics(report)
            info(f'Printing statistics for graph {graph_server.graph_name} on server {graph_server.url} for the past {report} seconds...')
            print(stats)
            info(f'Monitoring graph {graph_server.graph_name} on server {graph_server.url} every {ping} seconds started at {time.strftime("%b-%d-%Y %H:%M:%S", time.localtime(orig_time))}...')
            last_ping_time = current_time

    info('osiris monitor daemon stopped.')

@graph_server_cmd.command('query', help = 'Print graph server statistics')
@click.option('--text', default=None, help='Use this as the query text.')
@click.option('--file', type=click.Path(exists=True), default=None, help='Use the text in this file as the query text.')
@click.pass_context
def query_graph(ctx:click.Context, text, file):
    if text is None and file is None:
        exit_with_error('You must specify either the query text using --text or --file.')
    from core.graph_server import i as graph_server
    if text is not None:
        print(graph_server.query(text))
    else:
        with open(file, 'r') as f:
            print(graph_server.query(f.read()))