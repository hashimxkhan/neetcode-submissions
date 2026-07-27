class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        free = 0
        cur = []

        for cus in customers:
            if free <= cus[0]:
                cur.append(cus[1])
                free = cus[0] + cus[1]
            else:
                cur.append((free - cus[0] + cus[1]))
                free = free + cus[1]
        return sum(cur) / len(cur)
