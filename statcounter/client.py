from statcounter.clients.stats import StatsClient
from statcounter.clients.projects import ProjectsClient


class Statcounter(object):

    def __init__(self, username: str, password: str):
        self.stats = StatsClient(username, password)
        self.projects = ProjectsClient(username, password)
