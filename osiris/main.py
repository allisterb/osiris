import os, sys
import warnings
from logging import info,error

import osiris_global

# Needs corresponding entry in either PYTHONPATH or .env file for development.
sys.path.append(os.path.join(osiris_global.OSIRIS_DIR, 'ext'))

# Disable common warnings
warnings.filterwarnings("ignore", category=FutureWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning)

if __name__ == '__main__': 
    # Entry-point for CLI
    from cli.util import unhandled_exception_handler
    sys.excepthook = unhandled_exception_handler
    osiris_global.INTERACTIVE_CLI = True
    if '--debug' in sys.argv[1:]:
        osiris_global.DEBUG = True
        os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'
        info('Debug enabled.')
    else:
        os.environ['TF_CPP_MIN_LOG_LEVEL'] ='3'
    
    # Print logo
    from pyfiglet import Figlet
    from colorama import Fore,Style
    fig = Figlet(font='chunky')
    print(Fore.CYAN, fig.renderText('osiris')) 
    print('0.1.0' + os.linesep)
    print(Style.RESET_ALL)

    # Start thread to capture key press
    import threading
    threading.Thread(target=osiris_global.kb_capture_thread, args=(), name='kb_capture_thread', daemon=True).start()
    
    # Parse CLI commands
    from cli.commands import parse
    parse()