import os
import threading
from datetime import timedelta
from time import time
from logging import info, error, debug, warning
from queue import Queue

import click
from rich import print

import osiris_global
import data.gdelt
from base.timer import begin
from cli.commands import server as servercmd
from cli.util import exit_with_error

@servercmd.command(help='Monitor data sources and upload data to graph server.')  
@click.option('--id', default='osiris', help='The osiris instance id.')
@click.argument('source', default='gdelt')
@click.argument('target', default='tigergraph')
def monitor(id, source):
    osiris_global.OSIRIS_ID = id
    info(f'osiris instance id is {id}.')

    with begin('Connecting to server') as op:
        op.complete()

    message_queue = Queue()
    message_count = 0
    start_time = time()
    message_queue_thread = threading.Thread(target=data.gdelt_monitor.monitor, args=(message_queue), name='message_queue_thread', daemon=True)
    message_queue_thread.start()
    stop_monitoring_queue = False
    last_log_message = ''
    
    while ((not osiris_global.KBINPUT) and (not stop_monitoring_queue)):
        while not message_queue.empty():
            message = message_queue.get()
            if message == 'stop':
                stop_monitoring_queue = True
            else:
                #if server.process_ipfs_log_entry(message):
                    message_count += 1
        
        if not message_queue_thread.is_alive():
             exit_with_error(f'An error occurred monitoring the {source} data source.')
        
        running_time = time() - start_time
        if int(running_time) % 60 == 0:
            log_message = f'osiris server running in monitor mode for {timedelta(seconds=int(running_time))}. Processed {message_count} total log entries. Press [ENTER] to shutdown.'
            if not log_message == last_log_message: 
                info(f'osiris server running in monitor mode for {timedelta(seconds=int(running_time))}. Processed {message_count} total log entries. Press [ENTER] to shutdown.')
                last_log_message = log_message
    
    info("osiris server shutdown.")