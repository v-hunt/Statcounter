from urllib.parse import quote
from collections import namedtuple

import requests

from statcounter.url_builder import UrlBuilder
from statcounter import conf


SCProjectData = namedtuple('SCProjectData', ['project_id', 'security_code'])


class ProjectsClient(object):

    def __init__(self, username: str, password: str):
        self._username = username
        self._password = password

    def create(self, website_title: str, website_url: str,
               public_stats_level: int=1) -> SCProjectData:
        """
        Create a new project.

        Docs: http://statcounter.com/api/docs/v3#create-project

        public_stats_level:
            0: All public stats are disabled
            1: All stats are public
            2: Only 'Summary Stats' are public
        """
        url_builder = UrlBuilder(
            api_root=conf.API_ROOT,
            url_tail='add_project/',
            username=self._username, password=self._password,
            api_version=conf.API_VERSION_NUMBER,
        )
        params = {  # website_title and website_url should be urlencoded:
            'wt': quote(website_title),
            'wu': quote(website_url),
            'ps': public_stats_level,
        }

        url = url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()

        data = response.json()['sc_data'][0]
        return SCProjectData(
            project_id=data['project_id'],
            security_code=data['security_code'],
        )

    def increase_log_size(self, project_id: int, logsize: int) -> None:
        """
        Increase Project Log Size.

        Docs: http://statcounter.com/api/docs/v3#increase-logsize
        """
        url_builder = UrlBuilder(
            api_root=conf.API_ROOT,
            url_tail='update_logsize/',
            username=self._username, password=self._password,
            api_version=conf.API_VERSION_NUMBER,
        )
        params = {
            'pi': project_id,
            'ls': logsize,
        }

        url = url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()

    def retrieve_projects_details(self):
        """
        Retrieve details for ALL projects.

        Docs: http://statcounter.com/api/docs/v3#user-projects
        """
        url_builder = UrlBuilder(
            api_root=conf.API_ROOT,
            url_tail='user_projects/',
            username=self._username, password=self._password,
            api_version=conf.API_VERSION_NUMBER,
        )

        url = url_builder.build({})

        response = requests.get(url)
        response.raise_for_status()
        return response.json()['sc_data']

    def retrieve_selected_project_details(self, project_id: int):
        """
        Retrieve details for particular user's project.

        Docs: http://statcounter.com/api/docs/v3#select-project
        """
        url_builder = UrlBuilder(
            api_root=conf.API_ROOT,
            url_tail='select_project/',
            username=self._username, password=self._password,
            api_version=conf.API_VERSION_NUMBER,
        )
        params = {
            'pi': project_id,
        }

        url = url_builder.build(params)

        response = requests.get(url)
        response.raise_for_status()

        return response.json()['sc_data']
