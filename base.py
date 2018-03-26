class OpsGenieBase(object):
    """Base object for all OpsGenie API classes"""
    def __init__(self, api_key, url = 'https://api.opsgenie.com/v2/'):
        self.api_key = api_key
        self.url = url
