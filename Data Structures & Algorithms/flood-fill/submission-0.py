class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        original = image[sr][sc]
        rows, cols = len(image), len(image[0])
        seen = set()
        def dfs(r,c):
            if r >= rows or c >= cols or r < 0 or c < 0 or image[r][c] != original or (r,c) in seen:
                return
            image[r][c] = color
            seen.add((r,c))
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c-1)
            dfs(r,c+1)
        dfs(sr,sc)
        return image