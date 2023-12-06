test_cases = [
    {
        0: [1, 2, 5],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2, 5],
        5: [3, 0]
    }
]

def shortestPath(s, e, adjacency_list):
    queue = [(s, 0)]
    visited = set()
    res = float('inf')
    while queue:
        print(queue)
        cur = queue.pop(0)
        cur_id, dis = cur
        if cur_id == e:
            res = min(res, dis)
        visited.add(cur_id)
        dis += 1
        for child in adjacency_list.get(cur_id, []):
            if child in visited and child != e:
                continue
            queue.append((child, dis))
    return res
    


for example in test_cases:
    d = shortestPath(0,3,example)
    print(d)
