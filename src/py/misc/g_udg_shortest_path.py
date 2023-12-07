test_cases = [
    {
        0: [1, 2, 5],
        1: [0, 2],
        2: [0, 1, 3],
        3: [2, 5],
        5: [3, 0]
    },
    {
        0: [1, 4],
        1: [0, 2],
        2: [1, 3],
        3: [2, 4],
        4: [0, 3],
    }
]

def shortestPath(s, e, adjacency_list):
    queue = [(s, s, 0)]
    visited = set()
    origins = {}
    while queue:
        print(queue)
        orig, dest, dis = queue.pop(0)
        visited.add(dest)
        if dest not in origins:
            origins[dest] = (orig, dis)
        if dest == e:
            break
        dis += 1
        for child in adjacency_list.get(dest, []):
            if child in visited and child != e:
                continue
            queue.append((dest, child, dis))
    
    trace = [dest]
    cur = dest
    while cur != s:
        cur, _ = origins[cur]
        trace.append(cur)
    
    return dis, trace

    


for example in test_cases:
    d = shortestPath(0,3,example)
    print(d)
