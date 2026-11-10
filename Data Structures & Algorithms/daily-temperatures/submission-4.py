class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # monotonic stack
        stack = []
        ret = [0] * len(temperatures)
        for i, temp in enumerate(temperatures):
            if not stack or stack[-1][0] > temp:
                stack.append([temp, i])
                continue
            while stack and stack[-1][0] < temp:
                ind = stack[-1][1]
                ret[ind] = i - ind
                stack.pop()
            stack.append([temp,i])
        return ret
            
            
