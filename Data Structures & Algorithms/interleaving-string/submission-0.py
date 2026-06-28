class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        memo = {}

        def dp(i,j,k):
            if k == len(s3):
                if i == len(s1) and j == len(s2):
                    return True
                return False
            if (i,j,k) in memo:
                return memo[(i,j,k)]
            
            if i < len(s1) and s3[k] == s1[i]:
                if dp(i+1,j,k+1):
                    memo[(i,j,k)] = True
                    return True

            if j < len(s2) and s3[k] == s2[j]:
                if dp(i,j+1,k+1):
                    memo[(i,j,k)] = True
                    return True

            memo[(i,j,k)] = False
            return False
            
        return dp(0,0,0)