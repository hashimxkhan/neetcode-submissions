class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        opens = ["[", "{", "("]
        for c in s:
            if c in opens:
                stack.append(c)
            else:
                if not stack:
                    return False
                if c == "]":
                    if stack.pop() != "[":
                        return False
                if c == "}":
                    if stack.pop() != "{":
                        return False
                if c == ")":
                    if stack.pop() != "(":
                        return False
        
        if stack:
            return False
        return True