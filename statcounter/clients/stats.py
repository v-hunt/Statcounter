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

    def entry_pages(self, project_id: Union[int, List[int]],
                    chop_urls: bool=True, count_type: str='page_view',
                    date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#entry

        @count_type: should be 'page_view' or 'visitor'
        """

        # TODO: for now I can't see any difference when change chop_urls or count_type

        params = {
            's': 'entry',
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

    def exit_pages(self, project_id: Union[int, List[int]],
                   chop_urls: bool=True, count_type: str='page_view',
                   date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#exit
        """

        # TODO: for now I can't see any difference when change chop_urls or count_type

        params = {
            's': 'exit',
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

    def came_from(self, project_id: Union[int, List[int]],
                  exclude_search_engines: bool=False,
                  group_by_domain: bool=False,
                  date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#camefrom
        """

        # TODO: for now I can't see any difference when change chop_urls or count_type

        params = {
            's': 'camefrom',
            'pi': project_id,
            'n': n,
            'ese': int(exclude_search_engines),
            'gbd': int(group_by_domain),
        }

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']

    def recent_came_from(self, project_id: Union[int, List[int]],
                         exclude_search_engines: bool=False,
                         date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#recent_camefrom
        """
        params = {
            's': 'recent_camefrom',
            'pi': project_id,
            'n': n,
            'ese': int(exclude_search_engines),
        }

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']

    def recent_keyword_activity(
            self, project_id: Union[int, List[int]],
            exclude_encrypted_keywords: bool=False,
            exclude_external_results: bool=True,
            date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#keyword-activity
        """
        params = {
            's': 'keyword-activity',
            'pi': project_id,
            'n': n,
            'eek': int(exclude_encrypted_keywords),
            'e': int(exclude_external_results),
        }

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']

    def search_engines(
            self, project_id: Union[int, List[int]],
            date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#search_engine
        """
        params = {
            's': 'search_engine',
            'pi': project_id,
            'n': n,
        }

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']

    def recent_pageload_activity(
            self, project_id: Union[int, List[int]],
            date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#pageload
        """
        params = {
            's': 'pageload',
            'pi': project_id,
            'n': n,
        }

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']

    def visit_length(
            self, project_id: Union[int, List[int]],
            date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#visit-length
        """
        params = {
            's': 'visit_length',
            'pi': project_id,
            'n': n,
        }

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']

    def keyword_analysis(
            self, project_id: Union[int, List[int]],
            combine_keywords: str='search_engine_host',
            exclude_encrypted_keywords: bool=False,
            date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#keyword-analysis

        @combine_keywords: 'search_engine_host', 'search_engine_name' or 'together'
        """
        params = {
            's': 'keyword_analysis',
            'pi': project_id,
            'n': n,
            'ck': combine_keywords,
            'eek': bool(exclude_encrypted_keywords),
        }

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']
