def dfs(adj_ls, s):
    stack = [s]
    arr = []
    while stack:
        cur = stack.pop()
        print(cur)
        arr.append(cur)
        for child in adj_ls.get(cur, []):
            stack.append(child)
    
    return arr

adj_ls = {
    0: [1,2],
    1: [3,4],
    2: [5,8],
    5: [6,7]
}
arr = dfs(adj_ls, 0)
print(arr)