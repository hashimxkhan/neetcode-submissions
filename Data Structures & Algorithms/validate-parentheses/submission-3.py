from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        opening = ["(", "{", "["]
        mapping = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []
        
        for c in s:
            if c in opening:
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                cur = stack.pop()
                if mapping[cur] != c:
                    return False
        if len(stack) > 0: return False
        return True

        