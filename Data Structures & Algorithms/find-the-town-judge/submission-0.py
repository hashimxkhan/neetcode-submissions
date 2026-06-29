class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inDeg = {}
        outDeg = {}
        for i in range(1,n+1):
            inDeg[i] = 0
            outDeg[i] = 0
        
        for rel in trust:
            inDeg[rel[1]]+=1
            outDeg[rel[0]]+=1
        
        count = 0
        label = -1
        for person in inDeg:
            if inDeg[person] == n-1:
                if outDeg[person] == 0:
                    count+=1
                    label = person
                    
        if count == 1:
            return label
        return -1
