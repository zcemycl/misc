def grid_travel(i, j, count=0, target=()):
    if (i,j) == target:
        count += 1
        return count
    if i<target[0] or j<target[1]: return 0
    ci = grid_travel(i-1, j, count, target)
    cj = grid_travel(i, j-1, count, target)
    return ci + cj

print(grid_travel(3,2,0,target=(1,1)))
print(grid_travel(3,3,0,target=(1,1)))
print(grid_travel(3,3,0,target=(2,1)))
print(grid_travel(3,3,0,target=(2,2)))
