class Solution:
    def getTotalIsles(self, grid: list[list[str]]) -> int:
        def dfs(x, y):
            if x < 0 or y < 0 or x >= len(grid) or y >= len(grid[0]) or grid[x][y] != 'L':
                return
            grid[x][y] = 'W'
            dfs(x + 1, y)
            dfs(x - 1, y)
            dfs(x, y + 1)
            dfs(x, y - 1)
        if not grid:
            return 0
        num_islands = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 'L':
                    dfs(i, j)
                    num_islands += 1

        return num_islands
