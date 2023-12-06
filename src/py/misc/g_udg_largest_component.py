test_cases = [
    {
        0: [2],
        3: [7],
        7: [2],
        1: [5],
        4: [1,8],
        8: [5],
        6: [8]
    }
]

def convert_directed_to_undirected(adjacency_list):
    undirected_adjls = {}
    for key in adjacency_list:
        for e in adjacency_list[key]:
            undirected_adjls[key] = undirected_adjls.get(key, []) + [e]
            undirected_adjls[e] = undirected_adjls.get(e, []) + [key]
    return undirected_adjls

def recur(cur, count, adjacency_list, visited):
    if cur in visited:
        return count
    visited.add(cur)
    count += 1
    for child in adjacency_list.get(cur, []):
        count = recur(child, count, adjacency_list, visited)
    return count

def largest_component(num_of_nodes, adjacency_list):
    visited = set()
    res = 0
    for i in range(num_of_nodes):
        if i in visited:
            continue
        count = recur(i, 0, adjacency_list, visited)
        print(count)
        res = max(res, count)
    return res

for example in test_cases:
    c = largest_component(10, 
        convert_directed_to_undirected(example))
    print("Final result: ", c)
