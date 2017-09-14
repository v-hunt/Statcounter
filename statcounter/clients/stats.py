from typing import Union, List

import requests

from statcounter.clients.base import BaseClient
from statcounter.utils.date_range import DateRange

from typing import NewType

new = NewType('new', Union['aa', 'bb'])


class StatsClient(BaseClient):
    """
    API client for Retrieve Stats section:
    http://statcounter.com/api/docs/v3#retrieve-stats
    """

    @property
    def _url_tail(self):
        return 'stats/'

    def summary(self, project_id: Union[int, List[int]],
                date_range: Union[DateRange, None] = None):
        """
        Retrieve summary visits statistics.

        Docs: http://statcounter.com/api/docs/v3#summary
        """
        params = {
            's': 'summary',
            'pi': project_id,
        }

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']

    def recent_visitors(self, project_id: Union[int, List[int]],
                        date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#visitors
        """
        params = {
            's': 'visitor',
            'pi': project_id,
            'n': n,
        }

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']

    def popular_pages(self, project_id: Union[int, List[int]],
                      chop_urls: bool=True, count_type: str='page_view',
                      date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#popular

        @count_type: should be 'page_view' or 'visitor'
        """

        # TODO: for now I can't see any difference when change chop_urls or count_type

        params = {
            's': 'popular',
            'pi': project_id,
            'n': n,
            'c': int(chop_urls),
            'ct': count_type,
        }

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']
