class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        total = 0
        seats.sort()
        students.sort()
        for i in range(len(seats)):
            total+= abs(seats[i] - students[i])
        return total
