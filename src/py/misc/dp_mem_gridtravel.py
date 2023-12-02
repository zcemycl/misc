class Grid_Traveller:
    def __init__(self):
        self.reset()
    
    def reset(self):
        self.hist = {}
        self.count = 0

    def __call__(self, i, j, target=()):
        if (i,j) in self.hist:
            return self.hist[(i,j)]
        if (i,j) == target:
            self.count += 1
            return self.count
        if i<target[0] or j<target[1]: return 0
        ci = self.__call__(i-1, j, target)
        self.hist[(i-1,j)] = ci
        cj = self.__call__(i, j-1, target)
        self.hist[(i,j-1)] = cj
        return ci + cj

soln = Grid_Traveller()
print(soln(3,2,(1,1)))
print(soln.hist)
soln.reset()
for target in [(1,1), (2,1), (2,2)]:
    print(soln(3,3,target))
    print(soln.hist)
    soln.reset()
