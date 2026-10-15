class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in range(len(num) -1, -1, -1):
            stack.append(num[i])
        
        for i in range(k):
            stack.pop()
        while stack and stack[-1] == "0":
            stack.pop()
        if not stack:
            return "0"
        return ''.join(stack)[::-1]

