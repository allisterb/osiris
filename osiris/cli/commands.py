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
@click.argument('target')
@click.argument('url')
@click.argument('graph')
@click.option('--user', envvar='OSIRIS_GRAPH_SERVER_USER', default = None)
@click.option('--passwd', envvar='OSIRIS_GRAPH_SERVER_PASS', default = None)
@click.option('--token', envvar='OSIRIS_GRAPH_SERVER_TOKEN', default = None)
@click.pass_context
def graph_server(ctx, target, url, graph, user, passwd, token):
    if target != 'tg':
        exit_with_error('Only the TigerGraph graph database server is currently supported.')
    import core.graph_server
    ctx.obj['GRAPH_TARGET'] = core.graph_server.graph_target = target
    ctx.obj['GRAPH_API_URL'] = core.graph_server.graph_api_url = url
    ctx.obj['GRAPH_NAME'] = core.graph_name = graph
    ctx.obj['GRAPH_USER'] = core.graph_user = user
    ctx.obj['GRAPH_PASSWD'] = core.graph_passwd = passwd
    ctx.obj['GRAPH_TOKEN'] = core.graph_token = token

import cli.import_commands
import cli.monitor_commands
import cli.graph_server_commands