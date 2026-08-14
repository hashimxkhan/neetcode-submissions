class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        maps = {"a":a, "b":b, "c":c}
        ret = ""
        while True:
            if maps["a"] == 0 and maps["b"] == 0 and maps["c"] == 0:
                return ret
            ct = 0
            if maps["a"] == 0:
                ct+=1
            if maps["b"] == 0:
                ct+=1
            if maps["c"] == 0:
                ct+=1
            last = ""
            for key in maps:
                if maps[key] > 0:
                    last = key
            if ct == 2 and last == ret[len(ret) -  1] and last == ret[len(ret)-2]:
                return ret            
            cur = ""
            if maps["a"] >= maps["b"] and maps["a"] >= maps["c"]:
                cur = "a"
            elif maps["b"] >= maps["a"] and maps["b"] >= maps["c"]:
                cur = "b"
            else:
                cur = "c"
            
            if len(ret) >=2 and ret[len(ret) - 1] == cur and ret[len(ret)-2] == cur:
                if cur == "c":
                    if maps["a"] > maps["b"]:
                        cur = "a"
                    else:
                        cur = "b"    
                elif cur == "b":
                    if maps["a"] > maps["c"]:
                        cur = "a"
                    else:
                        cur = "c"  
                else:
                    if maps["b"] > maps["c"]:
                        cur = "b"
                    else:
                        cur = "c"
            maps[cur]-=1
            ret+=cur
             
