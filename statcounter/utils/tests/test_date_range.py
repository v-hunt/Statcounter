from unittest import TestCase

from statcounter.utils.date_range import DateRange


class DateRangeTestCase(TestCase):

    def test_yearly(self):
        date_range = DateRange.yearly(2016, 2017)

        expected_params = {
            'g': 'yearly',
            'sy': 2016,
            'ey': 2017,
        }

        self.assertDictEqual(
            date_range.params,
            expected_params,
        )

    def test_quarterly(self):
        date_range = DateRange.quarterly(2017, 1, 2018, 2)

        expected_params = {
            'g': 'quarterly',
            'sy': 2017,
            'sq': 1,
            'ey': 2018,
            'eq': 2,
        }

        self.assertDictEqual(
            date_range.params,
            expected_params,
        )

    def test_monthly(self):
        date_range = DateRange.monthly(1, 2017, 11, 2018)

        expected_params = {
            'g': 'monthly',
            'sm': 1,
            'sy': 2017,
            'em': 11,
            'ey': 2018,
        }

        self.assertDictEqual(
            date_range.params,
            expected_params,
        )

    def test_weekly(self):
        date_range = DateRange.weekly(2017, 1, 2018, 2)

        expected_params = {
            'g': 'weekly',
            'sy': 2017,
            'sw': 1,
            'ey': 2018,
            'ew': 2,
        }

        self.assertDictEqual(
            date_range.params,
            expected_params,
        )

    def test_daily(self):
        date_range = DateRange.daily(1, 9, 2017, 30, 10, 2017)

        expected_params = {
            'g': 'daily',
            'sd': 1,
            'sm': 9,
            'sy': 2017,
            'ed': 30,
            'em': 10,
            'ey': 2017,
        }

        self.assertDictEqual(
            date_range.params,
            expected_params,
        )

    def test_hourly(self):
        date_range = DateRange.hourly(1, 2, 10, 2017, 3, 5, 11, 2018)

        expected_params = {
            'g': 'hourly',
            'sh': 1,
            'sd': 2,
            'sm': 10,
            'sy': 2017,
            'eh': 3,
            'ed': 5,
            'em': 11,
            'ey': 2018,
        }

        self.assertDictEqual(
            date_range.params,
            expected_params,
        )
