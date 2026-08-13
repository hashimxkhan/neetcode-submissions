class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                val = ""
                cur = ""
                while val != "[":
                    val = stack.pop()
                    if val == "[":
                        break
                    cur = val + cur
                repeat = ""
                val = "0"
                while val in "0123456789" and stack:
                    val = stack.pop()
                    if val not in "0123456789":
                        stack.append(val)
                        break
                    repeat = val + repeat
                stack.append(int(repeat) * cur)
        
        ret = ""
        for c in stack:
            ret+=c
        return ret