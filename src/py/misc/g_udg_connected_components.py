test_cases = [
    {
        0: [2],
        2: [3,7],
        1: [4,5],
        4: [8],
        5: [8]
    }
]

def convert_directed_to_undirected(adjacency_list):
    undirected_adjls = {}
    for key in adjacency_list:
        for e in adjacency_list[key]:
            undirected_adjls[key] = undirected_adjls.get(key, []) + [e]
            undirected_adjls[e] = undirected_adjls.get(e, []) + [key]
    return undirected_adjls

def recur(cur, adjacency_list, visited):
    if cur in visited:
        return visited
    visited.add(cur)
    for child in adjacency_list.get(cur, []):
        visited = recur(child, adjacency_list, visited)
    return visited

def connected_components(num_of_nodes, adjacency_list):
    res = 0
    visited = set()
    for i in range(num_of_nodes):
        if i in visited:
            continue
        visited = recur(i, adjacency_list, visited)
        res += 1
    return res

for example in test_cases:
    c = connected_components(9, 
        convert_directed_to_undirected(example))
    print(c)
