class Solution:
    directions = [
        (1, 0), (-1, 0), (0, 1), (0, -1)
    ]
    @classmethod
    def naive(cls, grid):
        nrows = len(grid)
        ncols = len(grid[0])

        def dfs(i, j):
            if i<0 or i>ncols-1 or j<0 or\
                j>nrows-1 or grid[j][i] == "x":
                return 
            if grid[j][i] == "0":
                grid[j][i] = "x"
                return
            grid[j][i] = "x"
            
            for di,dj in cls.directions:
                dfs(i+di, j+dj)
        
        result = 0
        for j in range(nrows):
            for i in range(ncols):
                if grid[j][i] != "x" and grid[j][i] != "0":
                    dfs(i, j)
                    result += 1
        return result

            

if __name__ == "__main__":
    inputs = [
        ([
        ["1","1","1","1","0"],
        ["1","1","0","1","0"],
        ["1","1","0","0","0"],
        ["0","0","0","0","0"]
        ], 1),
        ([
        ["1","1","0","0","0"],
        ["1","1","0","0","0"],
        ["0","0","1","0","0"],
        ["0","0","0","1","1"]
        ], 3)
    ]
    for grid, expected in inputs:
        print(Solution.naive(grid))
        print("----")