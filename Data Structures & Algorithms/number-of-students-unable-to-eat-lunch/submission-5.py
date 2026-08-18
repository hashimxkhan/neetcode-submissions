class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        maps = {}
        sandwiches = deque(sandwiches)
        for s in students:
            if s not in maps:
                maps[s] = 0
            maps[s]+=1
        total = len(students)
        count = 0
        while True and sandwiches:
            cur = sandwiches[0]
            if cur not in maps or maps[cur] == 0:
                break
            else:
                maps[cur]-=1
                sandwiches.popleft()
                count+=1
        return len(students) - count
        
        