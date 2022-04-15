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
    if graph_server.token is not None:
        info(f'Graph server token is {graph_server.token[:2]}xxx...')
    info('Printing endpoints...')
    print(graph_server.get_info())
