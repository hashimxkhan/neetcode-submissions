class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        rows, cols = len(image), len(image[0])
        seen = set()
        pixel = image[sr][sc]
        def dfs(i, j, pixel):
            if (i < 0 or i >= rows or j < 0 or j >= cols or (i,j) in seen or image[i][j] != pixel):
                return
            image[i][j] = color
            seen.add((i,j))
            dfs(i+1, j, pixel)
            dfs(i-1, j, pixel)
            dfs(i, j+1, pixel)
            dfs(i, j-1, pixel)
        dfs(sr, sc, pixel)
        return image
        