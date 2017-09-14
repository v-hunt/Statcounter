from unittest import TestCase

from statcounter.clients.stats import StatsClient, DateRange
from requests.exceptions import HTTPError


DEMO_USERNAME = 'demo_user'
DEMO_API_PASSWORD = 'statcounter'
DEMO_PROJECT_ID = 2292634


class StatsClientTestCase(TestCase):

    def setUp(self):
        self.client = StatsClient(
            username=DEMO_USERNAME,
            password=DEMO_API_PASSWORD,
        )

    def test_summary(self):
        try:
            self.client.summary(project_id=DEMO_PROJECT_ID)
        except HTTPError:
            self.fail("Fail to retrieve summary data!")

    def test_summary_weekly(self):
        try:
            self.client.summary(
                project_id=DEMO_PROJECT_ID,
                date_range=DateRange.weekly(2017, 1, 2017, 10)
            )
        except HTTPError:
            self.fail("Fail to retrieve summary data!")

    def test_recent_visitors(self):
        try:
            self.client.recent_visitors(DEMO_PROJECT_ID)
        except HTTPError:
            self.fail("Fail to retrieve summary data!")

    def test_resent_visitors_weekly(self):
        try:
            self.client.recent_visitors(
                DEMO_PROJECT_ID,
                DateRange.weekly(2017, 1, 2017, 2)
            )
        except HTTPError:
            self.fail("Fail to retrieve summary data!")

    def test_popular_pages(self):
        try:
            self.client.popular_pages(DEMO_PROJECT_ID, chop_urls=False)
        except HTTPError:
            self.fail("Fail to retrieve summary data!")

    def test_entry_pages(self):
        try:
            self.client.entry_pages(DEMO_PROJECT_ID, chop_urls=False)
        except HTTPError:
            self.fail("Fail to retrieve summary data!")

    def test_exit_pages(self):
        try:
            self.client.exit_pages(DEMO_PROJECT_ID)
        except HTTPError:
            self.fail("Fail to retrieve summary data!")

    def test_came_from(self):
        try:
            self.client.came_from(DEMO_PROJECT_ID)
        except HTTPError:
            self.fail("Fail to retrieve summary data!")

    def test_recent_came_from(self):
        try:
            self.client.recent_came_from(DEMO_PROJECT_ID, n=20)
        except HTTPError:
            self.fail("Fail to retrieve summary data!")

    def test_recent_keyword_activity(self):
        try:
            self.client.recent_keyword_activity(DEMO_PROJECT_ID, n=100)
        except HTTPError:
            self.fail("Fail to retrieve summary data!")

