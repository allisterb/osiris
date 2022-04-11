import os
import json
import binascii
from datetime import datetime
from logging import info, error, debug
from tempfile import TemporaryDirectory

import osiris_global

graph_api_url = None
graph_user = None
graph_pass = None
graph_token = None