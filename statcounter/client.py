from statcounter.clients.stats import StatsClient
from statcounter.clients.projects import ProjectsClient
from statcounter.clients.account import AccountClient


class Statcounter(object):

    def __init__(self, username: str, password: str):
        self.stats = StatsClient(username, password)
        self.projects = ProjectsClient(username, password)
        self.account = AccountClient(username, password)
