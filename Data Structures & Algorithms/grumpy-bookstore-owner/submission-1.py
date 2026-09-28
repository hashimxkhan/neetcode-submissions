class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:

        def satisfied(customers, arr):
            ret = 0
            for i in range(len(customers)):
                if arr[i] == 0:
                    ret+= customers[i]

            return ret

        best = 0
        for i in range(len(grumpy) - minutes + 1):
            arr = grumpy[:]
            for j in range(i, i + minutes):
                arr[j] = 0
            
            best = max(best, satisfied(customers, arr))
        
        return best
                


        