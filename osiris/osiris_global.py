import os, sys
from logging import info,debug

DEBUG = False

OSIRIS_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))

OSIRIS_ID:str = ''

KBINPUT = False

INTERACTIVE_CLI = False

INTERACTIVE_NOTEBOOK = False

DAEMON = False

SCRIPT = False

def set_runtime_env(interactive_nb, debug=False):
        global DEBUG, INTERACTIVE_CLI, INTERACTIVE_NOTEBOOK, DAEMON, SCRIPT
        import logging
        logging.root.handlers.clear()
        if debug:
            DEBUG = True
            logging.basicConfig(format='%(message)s', datefmt='%I:%M:%S %p', stream=sys.stdout, level=logging.DEBUG)
            os.environ['TF_CPP_MIN_LOG_LEVEL'] = '0'  # or any {'0', '1', '2'}  to control TensorFlow 2 logging level
        else:
            DEBUG = False
            logging.basicConfig(format='%(message)s', datefmt='%I:%M:%S %p', stream=sys.stdout, level=logging.INFO)
            os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'  # or any {'0', '1', '2'}  to control TensorFlow 2 logging level
        if interactive_nb:
            INTERACTIVE_NOTEBOOK = True
            INTERACTIVE_CLI = False
            DAEMON = False
            SCRIPT = False

def kb_capture_thread():
    """Capture keyboard input"""
    global KBINPUT
    try:
        input()
        if not DAEMON:
            info("Enter key pressed...")
        else:
            info("osiris daemon stop requested...")
        #_ = getch.getch()
        KBINPUT = True
    except EOFError as _:
        info('Ctrl-C pressed...')
        KBINPUT = True
        if INTERACTIVE_CLI:
            info('Program stop requested.')

def tqdm_iter(i, **kwargs):
    if DEBUG:
        return i
    elif INTERACTIVE_CLI:
        from tqdm import tqdm
        return(tqdm(i, **kwargs))
    elif INTERACTIVE_NOTEBOOK:
        from  tqdm.notebook import tqdm_notebook
        return tqdm_notebook(i, **kwargs)
    else:
        return i

def tqdm_debug(t, x):
    if DEBUG:
        if INTERACTIVE_CLI or INTERACTIVE_NOTEBOOK:
            t.write(x)
        else:
            debug(x)