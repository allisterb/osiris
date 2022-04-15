from logging import info, error

import click
from click import Context
from rich import print

import core.graph_server
from cli.commands import graph_server as graph_server_cmd
from cli.util import *

@graph_server_cmd.command('info', help = 'Print info on graph server')
@click.pass_context
def info_cmd(ctx:Context):
    if core.graph_server.token is not None:
        info(f'Graph server token is {core.graph_server.token[:2]}...')
    print(core.graph_server.server.get_info())
