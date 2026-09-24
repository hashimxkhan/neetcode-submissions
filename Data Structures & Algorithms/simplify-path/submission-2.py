class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        i = 0
        while i < len(path):
            while i < len(path) and path[i] == "/":
                i+=1
            if i >= len(path):
                break
            s = ""
            flag = True
            if path[i] == ".":
                ct = ""
                while i < len(path) and path[i] == ".":
                    ct = ct + "."
                    i+=1

                if i < len(path) and path[i] != "/":
                    s = ct
                else:
                    flag = False
                    if len(ct) == 2:
                        if stack:
                            stack.pop()
                    elif len(ct) > 2:
                        stack.append(ct)
            if flag:
                while i < len(path) and path[i] != "/":
                    s = s + path[i]
                    i+=1
                stack.append(s)
        if not stack:
            return "/"
        ret = ""
        while stack:
            ret = "/" + stack.pop() + ret 
        return ret

                    




            