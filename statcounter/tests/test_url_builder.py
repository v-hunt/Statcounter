from unittest import TestCase

from statcounter.url_builder import UrlBuilder
from collections import OrderedDict


TEST_API_VERSION_NUMBER = 3
TEST_API_ROOT = "http://api.statcounter.com/"

TEST_URL_TAIL = 'stats'
TEST_USERNAME = 'demo_user'
TEST_PASSWORD = 'statcounter'


class UrlBuilderTestCase(TestCase):

    def setUp(self):
        self.url_builder = UrlBuilder(
            api_root=TEST_API_ROOT,
            url_tail=TEST_URL_TAIL,
            api_version=TEST_API_VERSION_NUMBER,
            username=TEST_USERNAME,
            password=TEST_PASSWORD,
        )

    def test__calculate_sha1(self):
        sha1 = UrlBuilder._calculate_sha1('Hello World')

        self.assertEqual(
            sha1,
            '0a4d55a8d778e5022fab701977c5d840bbc486d0'
        )

    def test___get_url_tail(self):
        url = 'http://example.com/?a=5&b=123'
        url_tail = UrlBuilder._get_url_tail(url)
        expected_url_tail = '?a=5&b=123'

        self.assertEqual(
            url_tail,
            expected_url_tail
        )

    def test__hash_the_url(self):
        url = "http://api.statcounter.com/stats/?vn=3&s=visitor&f=json&pi=2292634&n=10&t=1504534122&u=demo_user"
        expected_url_with_sha1 = 'http://api.statcounter.com/stats/?vn=3&s=visitor&f=json&pi=2292634&n=10&t=1504534122&u=demo_user&sha1=71797cacaab926ab028917652d986159d571056b'

        self.assertEqual(
            self.url_builder._hash_the_url(url),
            expected_url_with_sha1
        )

    def test_build_method(self):
        # Python Dict doesn't preserve order, so we use OrderedDict here:
        params = OrderedDict([
            ('s', 'visitor'),
            ('f', 'json'),
            ('pi', 2292634),
            ('n', 10),
            ('t', 1504534122),
        ])

        result_url = self.url_builder.build(params)

        expected_url = "http://api.statcounter.com/stats/?vn=3&s=visitor&f=json&pi=2292634&n=10&t=1504534122&u=demo_user&sha1=71797cacaab926ab028917652d986159d571056b"

        self.assertEqual(
            result_url,
            expected_url,
            "Url was not built properly!"
        )
