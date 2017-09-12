from statcounter.clients.base import BaseClient
from statcounter.url_builder import UrlBuilder
from statcounter import conf


class DateRangeParams(object):
    """
    Collection of builder for date range parameters

    See http://statcounter.com/api/docs/v3#date-range
    """

    @staticmethod
    def hourly(start_hour: int, start_day: int, start_month: int, start_year: int,
               end_hour: int, end_day: int, end_month: int, end_year: int) -> dict:

        return {
            'g': 'hourly',
            'sh': start_hour,
            'sd': start_day,
            'sm': start_month,
            'sy': start_year,
            'eh': end_hour,
            'ed': end_day,
            'em': end_month,
            'ey': end_year,
        }

    @staticmethod
    def daily(start_day: int, start_month: int, start_year: int,
              end_day: int, end_month: int, end_year: int):

        return {
            'g': 'daily',
            'sd': start_day,
            'sm': start_month,
            'sy': start_year,
            'ed': end_day,
            'em': end_month,
            'ey': end_year,
        }

    @staticmethod
    def weekly(start_year: int, start_week: int,
               end_year: int, end_week: int):
        return {
            'g': 'weekly',
            'sy': start_year,
            'sw': start_week,
            'ey': end_year,
            'ew': end_week,
        }

    @staticmethod
    def monthly(start_month: int, start_year: int,
                end_month: int, end_year: int):
        return {
            'g': 'monthly',
            'sm': start_month,
            'sy': start_year,
            'em': end_month,
            'ey': end_year,
        }

    @staticmethod
    def quarterly(start_year: int, start_quarter: int,
                  end_year: int, end_quarter: int):
        return {
            'g': 'quarterly',
            'sy': start_year,
            'sq': start_quarter,
            'ey': end_year,
            'eq': end_quarter,
        }

    @staticmethod
    def yearly(start_year: int, end_year: int):
        return {
            'g': 'yearly',
            'sy': start_year,
            'ey': end_year,
        }


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
