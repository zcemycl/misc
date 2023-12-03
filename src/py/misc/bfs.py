def bfs(adj_ls, s):
    fifo = [s]
    arr = []
    while fifo:
        cur = fifo.pop(0)
        print(cur)
        arr.append(cur)
        for child in adj_ls.get(cur, []):
            fifo.append(child)
    
    return arr

adj_ls = {
    0: [1,2],
    1: [3,4],
    2: [5,8],
    5: [6,7]
}
arr = bfs(adj_ls, 0)
print(arr)