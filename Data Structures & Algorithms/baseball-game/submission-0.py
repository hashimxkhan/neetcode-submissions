class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = []
        for i in operations:
            if i == "D":
                cur = stack[-1] * 2
                stack.append(cur)
            elif i == "C":
                stack.pop()
            elif i == "+":
                cur = stack[-1] + stack[-2]
                stack.append(cur)
            else:
                stack.append(int(i))
        
        ret = 0
        while stack:
            ret+=stack.pop()
        return ret
