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


print(hasPath("j", "k", test_cases[0], set()))
print(hasPath("i", "j", test_cases[0], set()))
print(hasPath("a", "d", test_cases[1], set()))