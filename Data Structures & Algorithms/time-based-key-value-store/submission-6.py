class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        ret = ""
        if key not in self.store:
            return ret
        curKey = self.store[key]
        for i in range(len(curKey)):
            if curKey[i][1] <= timestamp:
                ret = curKey[i][0]
            else:
                break
        return ret

        
