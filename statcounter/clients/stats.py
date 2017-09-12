from statcounter.clients.base import BaseClient
from statcounter.utils.date_range import DateRange


class Stats(BaseClient):
    """
    API client for Retrieve Stats section:
    http://statcounter.com/api/docs/v3#retrieve-stats
    """

    @property
    def _url_tail(self):
        return 'stats/'

    def stats(self):
        pass
