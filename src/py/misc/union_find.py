class UnionFind:
    def __init__(self, num_of_nodes):
        self.num_of_nodes = num_of_nodes
        self.parent = self.makeHashTable(self.num_of_nodes)
        self.size = [1]*num_of_nodes
        self.count = num_of_nodes

    def makeHashTable(self, num_of_nodes):
        return {i: i for i in range(num_of_nodes)}

    def find(self, n):
        while n != self.parent[n]:
            # self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n

    def union(self, n1, n2):
        r1 = self.find(n1)
        r2 = self.find(n2)

        if r1 == r2:
            return
        
        if self.size[r1] > self.size[r2]:
            self.parent[r2] = r1
            self.size[r1] += 1
        else:
            self.parent[r1] = r2
            self.size[r2] += 1
        
        self.count -= 1

    
# edges = [
#     [0, 2],
#     [1, 4],
#     [1, 5],
#     [2, 3],
#     [2, 7],
#     [4, 8],
#     [5, 8],
# ]
edges = [
    [0, 1],
    [1, 2],
    [2, 3],
    [3, 4],
    [4, 5],
    [5, 6],
    [6, 7],
    [7, 8],
    [8, 0]
]
numberOfElements = 9

uf = UnionFind(9)

for node1, node2 in edges:
    uf.union(node1, node2)

print("number of connected components", uf.count)
print(uf.parent)
print(uf.size)
print(uf.count)