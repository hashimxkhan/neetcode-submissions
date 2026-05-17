class TimeMap:

    def __init__(self):
        self.hash = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hash:
            self.hash[key] = []
        self.hash[key].append([value, timestamp])   

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hash:
            return ""
        
        vals = self.hash[key]
        l = 0
        r = len(vals) - 1
        rec = -1
        while l <= r:
            m = (l+r) // 2
            print(m)
            if timestamp < vals[m][1]:
                r = m - 1
            else:
                l = m+1
                rec = m
        if rec > -1:
            return vals[rec][0]
        return ""

        
