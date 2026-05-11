class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        # doing O(1) SPACE
        return sorted(s) == sorted(t)
        
