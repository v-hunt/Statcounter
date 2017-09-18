from urllib.parse import quote
from collections import namedtuple

import requests

from statcounter.url_builder import UrlBuilder
from statcounter import conf


class AccountClient(object):

    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    def retrieve_log_size(self):
        """
        Retrieve Account Log Sizes.

        Docs: http://statcounter.com/api/docs/v3#retrieve-logsizes
        """
        url_builder = UrlBuilder(
            api_root=conf.API_ROOT,
            url_tail='account_logsizes/',
            username=self._username, password=self._password,
            api_version=conf.API_VERSION_NUMBER,
        )

        url = url_builder.build({})

        response = requests.get(url)
        response.raise_for_status()

        return response.json()['sc_data']

    def retrieve_user_details(self):
        """
        Retrieve User Details.

        Docs: http://statcounter.com/api/docs/v3#user-details
        """
        url_builder = UrlBuilder(
            api_root=conf.API_ROOT,
            url_tail='user_details/',
            username=self._username, password=self._password,
            api_version=conf.API_VERSION_NUMBER,
        )

        url = url_builder.build({})

        response = requests.get(url)
        response.raise_for_status()

        return response.json()['sc_data']
