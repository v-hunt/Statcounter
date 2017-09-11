import time
import hashlib


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

    @staticmethod
    def _urlize_multiple_pi_params(pi_values):
        pi_values = map(str, pi_values)
        return '&pi=' + '&pi='.join(pi_values)

    def build(self, params: dict):
        if 't' not in params:
            params['t'] = self._get_now_time()

        if 'f' not in params:
            params['f'] = 'json'

        multi_pi_url_part = None
        if 'pi' in params:
            if isinstance(params['pi'], list):
                multi_pi_url_part = self._urlize_multiple_pi_params(
                    params.pop('pi')
                )

        if not multi_pi_url_part:
            url = self.base_url + \
                  '?vn=' + str(self.api_version_number) + \
                  '&' + self._urlize_params(params) + \
                  '&u=' + self.username
        else:
            url = self.base_url + \
                  '?vn=' + str(self.api_version_number) + \
                  '&' + self._urlize_params(params) + \
                  multi_pi_url_part + \
                  '&u=' + self.username
        return self._hash_the_url(url)
