class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 1:
            return ["()"]
        ret = []
        def bt(arr, op, close):
            if op == close == n:
                ret.append("".join(arr))
                return
            if op < n:
                arr.append('(')
                bt(arr, op+1, close)
                arr.pop()
            if close < op:
                arr.append(')')
                bt(arr, op, close+1)
                arr.pop()

        bt([], 0, 0)  
        return ret     
        
        
        