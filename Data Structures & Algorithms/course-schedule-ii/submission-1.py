class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj = {}
        state = []
        output = []
        for i in range(numCourses):
            adj[i] = []
            state.append(0)
        for course, pre in prerequisites:
            adj[pre].append(course)
         

        def dfs(course):
            if state[course] == 1:
                return False
            if state[course] == 2:
                return True

            state[course] = 1 # visiting
            for nei in adj[course]:
                if not dfs(nei):
                    return False
            
            state[course] = 2 # visited
            output.append(course)
            return True
            

        for i in range(numCourses):
            if not dfs(i):
                return []
        return output[::-1]