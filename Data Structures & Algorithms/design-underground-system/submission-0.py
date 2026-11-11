class UndergroundSystem:
    def __init__(self):
        self.durations = {}
        self.ins = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.ins[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStation, startTime = self.ins[id]
        totalTime = t - startTime
        if (startStation, stationName) not in self.durations:
            self.durations[startStation, stationName] = [totalTime, 1]
        else:
            avg, n = self.durations[startStation, stationName]
            new = ((avg * n) + totalTime) / (n + 1)
            self.durations[startStation, stationName] = [new, n+1]
            
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        return self.durations[startStation, endStation][0]
