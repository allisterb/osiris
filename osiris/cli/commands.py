import click

from cli.logging import set_log_level
    
@click.group()
@click.option('--debug', is_flag=True, callback=set_log_level, expose_value=False)
def parse(): pass

@parse.group('import', help  = 'Import data from the specified data source.')
def data_import(): pass

@parse.group(help  = 'Start the osiris server.')
def server(): pass

import cli.import_commands
import cli.server_commands