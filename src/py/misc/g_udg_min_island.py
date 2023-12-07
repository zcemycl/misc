test_cases = [
    [
        [1,0,1,1,1,1],
        [0,1,1,1,1,0],
        [0,0,1,1,0,0],
        [1,1,0,0,1,0]
    ],
    [
        [1,1,0,0,1,1],
        [1,1,0,0,1,1],
        [1,1,0,0,0,1],
    ]
]

class Solution:
    def __init__(self, grid):
        self.grid = grid
        rows = len(self.grid)
        cols = len(self.grid[0])
        self.rows = rows
        self.cols = cols
        self.res = float('inf')
        self.visited = set()
        self.dir = [
            (1,0), (-1,0), (0,1), (0,-1)
        ]

    def recur(self, i, j):
        if i<0 or j<0 or \
            i>self.cols-1 or j>self.rows-1:
            return 0
        if (i,j) in self.visited:
            return 0
        self.visited.add((i,j))
        if self.grid[j][i] == 0:
            return 0
        acc = 1
        for di, dj in self.dir:
            acc += self.recur(i+di, j+dj)
        return acc
    
    def __call__(self):
        for j in range(self.rows):
            for i in range(self.cols):
                if (i,j) in self.visited:
                    continue
                if self.grid[j][i] == 0:
                    continue
                landmass = self.recur(i,j)
                print("new", i,j, landmass)
                self.res = min(self.res, landmass)
        return self.res

for grid in test_cases:
    soln = Solution(grid)
    print(soln())

