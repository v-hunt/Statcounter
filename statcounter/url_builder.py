import time
import hashlib
from collections import OrderedDict

from requests import PreparedRequest


class UrlBuilder(object):

    def __init__(self,
                 api_root: str, url_tail: str,
                 username: str, password: str,
                 api_version: int = 3
                 ):
        self.base_url = self._add_slash(api_root) + self._add_slash(url_tail)
        self.api_version_number = api_version
        self.username = username
        self.password = password

    @staticmethod
    def _add_slash(string: str):
        return string if string.endswith('/') else string + '/'

    @staticmethod
    def _get_now_time():
        """
        Get time of execution in Unix timestamp format.
        """
        return int(time.time())

    @staticmethod
    def _calculate_sha1(string: str) -> str:
        return hashlib.sha1(string.encode()).hexdigest()

    @staticmethod
    def _get_url_tail(url: str) -> str:
        return '?' + url.split('?')[1]

    def _hash_the_url(self, url: str) -> str:
        url_tail = self._get_url_tail(url)
        sha1 = self._calculate_sha1(url_tail + self.password)
        return url + '&sha1=' + sha1

    @staticmethod
    def _urlize_params(params: dict):
        series = ["{key}={value}".format(key=key, value=value)
                  for key, value in params.items()]
        return '&'.join(series)

    def build(self, params: dict):
        if 't' not in params:
            params['t'] = self._get_now_time()

        if 'f' not in params:
            params['f'] = 'json'

        # TODO: Add possibility to use multiple project ids
        url = self.base_url + \
              '?vn=' + str(self.api_version_number) + \
              '&' + self._urlize_params(params) + \
              '&u=' + self.username
        return self._hash_the_url(url)
