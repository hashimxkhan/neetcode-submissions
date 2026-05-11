class TimeMap:

    def __init__(self):
        self.store = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        if key not in self.store:
            return res
        times = self.store[key]
        l,r = 0, len(times)-1
        while l <= r:
            m = (l + r) // 2
            if times[m][1] <= timestamp:
                res = times[m][0]
                l = m + 1
            else:
                r = m - 1
        return res
        
        
