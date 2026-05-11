class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preReqs = {}
        for course, pre in prerequisites:
            if course not in preReqs:
                preReqs[course] = []
            preReqs[course].append(pre)
        
        visiting = set()
        def dfs(course):
            if course in visiting:
                return False
            if course not in preReqs:
                return True
            if preReqs[course] == []:
                return True
            visiting.add(course)
            for pre in preReqs[course]:
                if not dfs(pre):
                    return False
            visiting.remove(course)
            preReqs[course] = []
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        return True


        