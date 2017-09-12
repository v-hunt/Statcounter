from abc import ABC, abstractmethod

from statcounter.url_builder import UrlBuilder
from statcounter import conf


class BaseClient(ABC):
    """
    API client for Retrieve Stats section:
    http://statcounter.com/api/docs/v3#retrieve-stats
    """

    def __init__(self, username: str, password: str):

        self._url_builder = UrlBuilder(
            api_root=conf.API_ROOT,
            url_tail=self._url_tail,
            username=username, password=password,
            api_version=conf.API_VERSION_NUMBER,
        )

    @property
    @abstractmethod
    def _url_tail(self) -> str:
        """
        Set the url tail for concrete api section (e.g. 'stats/')
        """
        pass
