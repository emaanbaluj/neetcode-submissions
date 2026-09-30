class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        ROWS, COLS = len(grid), len(grid[0])


        directions = [(0,1), (1,0), (0,-1), (-1,0)]
        

        def dfs(i, j):

            if i >= ROWS or i < 0 or j >= COLS or j < 0:
                return 

            if grid[i][j] == "0":
                return

            grid[i][j] = "0"

            for (dr, dc) in directions:
                dfs(i + dr, j + dc)

   
        islands = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):

                if grid[i][j] == "1":
                    dfs(i,j)
                    islands += 1

        return islands
