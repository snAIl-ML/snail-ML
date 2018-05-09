class AIChecker(object):
    def __init__(self, status):
        self.flag = status

    def set_flag(self, status):
        self.flag = status

    def get_flag(self):
        return self.flag
