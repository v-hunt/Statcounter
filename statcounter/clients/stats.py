from typing import Union, List

import requests

from statcounter.clients.base import BaseClient
from statcounter.utils.date_range import DateRange


class StatsClient(BaseClient):
    """
    API client for Retrieve Stats section:
    http://statcounter.com/api/docs/v3#retrieve-stats
    """

    @property
    def _url_tail(self):
        return 'stats/'

    def _perform_request(self,
                         search_param: str,
                         project_id: Union[int, List[int]],
                         date_range: Union[DateRange, None]=None,
                         n: int=20,
                         include_n: bool=True,
                         **additional_params):

        params = {
            's': search_param,
            'pi': project_id,
            'n': n,
        }

        if not include_n:
            params.pop('n')

        params.update(additional_params)

        if date_range:
            params.update(date_range.params)

        url = self._url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']

    def summary(self, project_id: Union[int, List[int]],
                date_range: Union[DateRange, None] = None, n: int=20):
        """
        Retrieve summary visits statistics.

        Docs: http://statcounter.com/api/docs/v3#summary
        """
        return self._perform_request(
            'search_engine', project_id, date_range, n
        )

    def recent_visitors(self, project_id: Union[int, List[int]],
                        date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#visitors
        """
        return self._perform_request('visitor', project_id, date_range, n)

    def popular_pages(self, project_id: Union[int, List[int]],
                      chop_urls: bool=True, count_type: str='page_view',
                      date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#popular

        @count_type: should be 'page_view' or 'visitor'
        """

        # TODO: for now I can't see any difference when change chop_urls or count_type

        return self._perform_request(
            'popular', project_id, date_range, n,
            c=int(chop_urls),
            ct=count_type,
        )

    def entry_pages(self, project_id: Union[int, List[int]],
                    chop_urls: bool=True, count_type: str='page_view',
                    date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#entry

        @count_type: should be 'page_view' or 'visitor'
        """

        # TODO: for now I can't see any difference when change chop_urls or count_type

        return self._perform_request(
            'entry', project_id, date_range, n,
            c=int(chop_urls),
            ct=count_type,
        )

    def exit_pages(self, project_id: Union[int, List[int]],
                   chop_urls: bool=True, count_type: str='page_view',
                   date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#exit
        """

        # TODO: for now I can't see any difference when change chop_urls or count_type

        self._perform_request(
            'exit', project_id, date_range, n,
            c=int(chop_urls),
            ct=count_type,
        )

    def came_from(self, project_id: Union[int, List[int]],
                  exclude_search_engines: bool=False,
                  group_by_domain: bool=False,
                  date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#camefrom
        """

        # TODO: for now I can't see any difference when change chop_urls or count_type

        self._perform_request(
            'camefrom', project_id, date_range, n,
            ese=int(exclude_search_engines),
            gbd=int(group_by_domain),
        )

    def recent_came_from(self, project_id: Union[int, List[int]],
                         exclude_search_engines: bool=False,
                         date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#recent_camefrom
        """
        return self._perform_request(
            'recent_camefrom', project_id, date_range, n,
            ese=int(exclude_search_engines),
        )

    def recent_keyword_activity(
            self, project_id: Union[int, List[int]],
            exclude_encrypted_keywords: bool=False,
            exclude_external_results: bool=True,
            date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#keyword-activity
        """
        return self._perform_request(
            'keyword-activity', project_id, date_range, n,
            eek=int(exclude_encrypted_keywords),
            e=int(exclude_external_results),
        )

    def search_engines(
            self, project_id: Union[int, List[int]],
            date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#search_engine
        """
        return self._perform_request(
            'search_engine', project_id, date_range, n
        )

    def recent_pageload_activity(
            self, project_id: Union[int, List[int]],
            date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#pageload
        """
        return self._perform_request(
            'search_engine', project_id, date_range, n
        )

    def visit_length(
            self, project_id: Union[int, List[int]],
            date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#visit-length
        """
        return self._perform_request(
            'search_engine', project_id, date_range, n
        )

    def keyword_analysis(
            self, project_id: Union[int, List[int]],
            combine_keywords: str='search_engine_host',
            exclude_encrypted_keywords: bool=False,
            date_range: Union[DateRange, None]=None, n: int=20):
        """
        Docs: http://statcounter.com/api/docs/v3#keyword-analysis

        @combine_keywords: 'search_engine_host', 'search_engine_name' or 'together'
        """
        return self._perform_request(
            'search_engine', project_id, date_range, n,
            ck=combine_keywords,
            eek=bool(exclude_encrypted_keywords),
        )
