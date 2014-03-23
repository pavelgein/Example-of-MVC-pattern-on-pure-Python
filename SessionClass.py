class Session(object):
    def __init__(self):
        self._NextId = 1
        self._Storage = {}
    def AddNewSession(self, info):
        self._Storage[self._NextId] = info
        self._NextId += 1
        return self._NextId - 1
    def UpdateInfo(self, id, field, newInfo):
        self._Storage[id][field] = newInfo
    def GetInfo(self, id, field):
        return self._Storage[id][field]
    def goodSession(self, sessionId):
        try:
            info = self._Storage[sessionId]
            return info['auth'] == True or info['num'] < 3
        except KeyError:
            return False
    def existsSession(self, sessionId):
        ans = sessionId in self._Storage
        return ans

