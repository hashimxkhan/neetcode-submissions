class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        maps = {}
        for stu in students:
            if stu not in maps:
                maps[stu] = 0
            maps[stu]+=1
        
        count = 0
        while True and sandwiches:
            num = sandwiches[0]
            if num not in maps or maps[num] == 0:
                break
            else:
                maps[num]-=1
                count+=1
                sandwiches.pop(0)
        return len(students) - count

                