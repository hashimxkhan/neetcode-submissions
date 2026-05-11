class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build adj list
        adj = {}
        for i in range(numCourses):
            adj[i] = []
        for course, pre in prerequisites:
            adj[pre].append(course)
        
        state = [0] * numCourses

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True
            
            state[course] = 1

            for nei in adj[course]:
                if not dfs(nei):
                    return False
            state[course] = 2
            return True

        




        for course in adj:
            if not dfs(course):
                return False
        return True
