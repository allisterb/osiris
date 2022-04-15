import click

from cli.logging import set_log_level
from cli.util import exit_with_error
    
@click.group()
@click.option('--debug', is_flag=True, callback=set_log_level)
@click.pass_context
def parse(ctx, debug):
    ctx.ensure_object(dict)
    ctx.obj['DEBUG'] = debug

@parse.group('import', help  = 'Bulk import data from data sources.')
def data_import(): pass

@parse.group(help  = 'Start a daemon process to monitor data sources and upload data to graph server.')
def monitor(): pass

@parse.group('graph', help  = 'Run commands and queries on a graph server.')
@click.argument('url')
@click.argument('graph_name')
@click.option('--target', default='tg')
@click.option('--user', envvar='OSIRIS_GRAPH_SERVER_USER', default = None)
@click.option('--passwd', envvar='OSIRIS_GRAPH_SERVER_PASS', default = None)
@click.option('--token', envvar='OSIRIS_GRAPH_SERVER_TOKEN', default = None)
@click.pass_context
def graph_server(ctx, url, graph_name, target, user, passwd, token):
    if target != 'tg':
        exit_with_error('Only the TigerGraph graph server is currently supported.')
    import core.graph_server
    ctx.obj['GRAPH_API_URL'] = core.graph_server.api_url = url
    ctx.obj['GRAPH_NAME'] = core.graph_server.graph_name = graph_name
    ctx.obj['GRAPH_TARGET'] = core.graph_server.target = target
    ctx.obj['GRAPH_USER'] = core.graph_server.user = user
    ctx.obj['GRAPH_PASSWD'] = core.graph_server.passwd = passwd
    ctx.obj['GRAPH_TOKEN'] = core.graph_server.token = token

import cli.import_commands
import cli.monitor_commands
import cli.graph_server_commands