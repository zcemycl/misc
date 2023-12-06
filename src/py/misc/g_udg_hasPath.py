test_cases = [
    {
        "f": ["g", "i"],
        "g": ["h"],
        "i": ["g", "k"],
        "j": ["i"]
    },
    {
        "a": ["b"],
        "b": ["c"],
        "c": ["a", "d"],
    }
]

def convert_directed_to_undirected(adjacency_list):
    undirected_adjls = {}
    for key in adjacency_list:
        for e in adjacency_list[key]:
            undirected_adjls[key] = undirected_adjls.get(key, []) + [e]
            undirected_adjls[e] = undirected_adjls.get(e, []) + [key]
    return undirected_adjls

def hasPath(s, e, adjacency_list, visited):
    if s == e:
        return True
    if s in visited:
        return False
    
    visited.add(s)
    for child in adjacency_list.get(s,[]):
        if hasPath(child, e, adjacency_list, visited):
            return True
    return False

print(hasPath("j", "k", 
    convert_directed_to_undirected(test_cases[0]), 
    set()))
print(hasPath("i", "j", 
    convert_directed_to_undirected(test_cases[0]), 
    set()))
print(hasPath("a", "d", 
    convert_directed_to_undirected(test_cases[1]), 
    set()))