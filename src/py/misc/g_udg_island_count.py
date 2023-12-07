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
        self.res = 0
        self.visited = set()
        self.dir = [
            (1,0), (-1,0), (0,1), (0,-1)
        ]

    def recur(self, i, j):
        if i<0 or j<0 or \
            i>self.cols-1 or j>self.rows-1:
            return
        if (i,j) in self.visited:
            return
        self.visited.add((i,j))
        if self.grid[j][i] == 0:
            return
        for di, dj in self.dir:
            self.recur(i+di, j+dj)
    
    def __call__(self):
        for j in range(self.rows):
            for i in range(self.cols):
                if (i,j) in self.visited:
                    continue
                if self.grid[j][i] == 0:
                    continue
                print("new", i,j)
                self.recur(i,j)
                self.res += 1
        return self.res

for grid in test_cases:
    soln = Solution(grid)
    print(soln())

