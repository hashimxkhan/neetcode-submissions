class Solution:
    def isValid(self, s: str) -> bool:
        mapping = { ']' : '[', '}' : '{', ')' : '(' }
        opening = "[{("
        stack = []
        for bracket in s:
            if bracket in opening:
                stack.append(bracket)
                continue

            if not stack or stack[-1] != mapping[bracket]:
                return False
            else:
                stack.pop()
        if stack:
            return False
        return True

