from email.policy import default
from logging import info, error

import click
from rich import print

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
    info('Printing endpoints...')
    print(graph_server.get_info())

@graph_server_cmd.command('stats', help = 'Print graph server statistics')
@click.argument('seconds', default=59)
@click.pass_context
def statistics(ctx:click.Context, seconds):
    from core.graph_server import i as graph_server
    info(f'Printing statistics for graph server {graph_server.url} for the past {seconds} seconds...')
    print(graph_server.get_statistics(seconds))
