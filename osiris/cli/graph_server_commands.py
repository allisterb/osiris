from logging import info, error

import click
from click import Context
from rich import print

import core.graph_server
from cli.commands import graph_server as graph_server_cmd
from cli.util import *

@graph_server_cmd.command('info', help = 'Print info on graph server')
@click.pass_context
def info(ctx:Context):
    
    print(core.graph_server.graph_api_url)
    #print(graph_server)
    #if token is not None:
    #    info(f'Graph server token is {token[:2]}...')
