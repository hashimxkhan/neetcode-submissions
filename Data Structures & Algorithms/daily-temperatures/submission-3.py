class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        ret = [0] * len(temperatures)
        stack.append([temperatures[0], 0])
        for i in range(1,len(temperatures)):
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                cur = stack.pop()
                ret[cur[1]] = i - cur[1]
            stack.append([temperatures[i], i])
        return ret