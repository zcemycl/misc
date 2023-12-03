def dfs(adj_ls, s, arr):
    print(s) 
    arr.append(s)
    if len(adj_ls.get(s, [])) == 0:
        return
    for child in adj_ls[s]:
        dfs(adj_ls, child, arr)

adj_ls = {
    0: [1,2],
    1: [3,4],
    2: [5,8],
    5: [6,7]
}
ptarr = []
dfs(adj_ls, 0, ptarr)
print(ptarr)