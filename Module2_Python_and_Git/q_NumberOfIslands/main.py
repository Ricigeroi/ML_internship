class Solution:
    def num_islands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])
        def dfs(i, j):
            grid[i][j] = '0'
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if (0 <= x < n) and (0 <= y < m) and (grid[x][y] == '1'):
                    dfs(x, y)

        count = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    count += 1
                    dfs(i, j)

        return count
