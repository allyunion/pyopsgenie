#!/usr/bin/python3

# Standard Library imports

# Custom Library imports
from base import OpsGenieBase

class Alert(OpsGenieBase):
    def __init__(self, api_key, url = 'https://api.opsgenie.com/v2/', alert_id=None):

