

# There is only api version 3 available at the moment:
API_VERSION_NUMBER = 3
API_ROOT = "http://api.statcounter.com/"


class Statcounter(object):

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password

    def stats(self):
        pass
