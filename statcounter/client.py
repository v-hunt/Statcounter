from statcounter.url_builder import UrlBuilder

# There is only api version 3 available at the moment:
API_VERSION_NUMBER = 3
API_ROOT = "http://api.statcounter.com/"


class Statcounter(object):

    def __init__(self, username: str, password: str):

        self._url_builder = UrlBuilder(
            api_root=API_ROOT,
            url_tail='stats/',
            username=username, password=password,
            api_version=API_VERSION_NUMBER,
        )

    def stats(self):
        pass
