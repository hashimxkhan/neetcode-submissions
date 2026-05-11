class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preReqs = {}
        for i in range(numCourses):
            preReqs[i] = []
        for crs, pre in prerequisites:
            preReqs[crs].append(pre)
        visiting = set()
        visited = set()
        res = []
        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True
            visiting.add(crs)
            for pre in preReqs[crs]:
                if dfs(pre) == False:
                    return False
            visiting.remove(crs)
            visited.add(crs)
            res.append(crs)
            return True
        
        for i in range(numCourses):
            if dfs(i) == False:
                return []
        return res