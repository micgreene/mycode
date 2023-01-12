#!/usr/bin/env python3

"""
Requests Practice | Author: Mike Greene
An example of requesting data from a flask api and converting the JSON back to Python
"""

import requests
from pprint import pprint

# api URL
api = "http://127.0.0.1:2224/page1"

# convert take response and turn it into Python data
resp = requests.get(api).json()

# print results
pprint(resp)
