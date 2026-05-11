class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        stack = []
        cur = 0
        for i in range(len(temperatures)):
            if i == 0:
                stack.append([temperatures[i], i])
                continue
            while len(stack) > 0 and temperatures[i] > stack[-1][0]:
                prev = stack.pop()
                result[prev[1]] = i - prev[1]
            stack.append([temperatures[i], i])

        return result

            