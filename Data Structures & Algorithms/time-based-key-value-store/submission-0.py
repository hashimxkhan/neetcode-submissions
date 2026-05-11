class TimeMap:

    def __init__(self):
        self.keystore = {} # key: list of [value, timestamp]

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keystore:
            self.keystore[key] = []
        self.keystore[key].append([value, timestamp])
        
    def get(self, key: str, timestamp: int) -> str:
        ans = ""
        if key not in self.keystore:
            return ""
        arr = self.keystore.get(key, [])
        l, h = 0, len(arr) - 1
        while l <= h:
            m = (l + h) // 2
            if arr[m][1] <= timestamp:
                ans = arr[m][0]
                l = m+1
            else:
                h = m-1
        return ans
        
