class Solution:
    @classmethod
    def naive(cls, n, edges):
        adjls = {}
        for u,v in edges:
            adjls[u] = adjls.get(u,[])+[v]
            adjls[v] = adjls.get(v,[])+[u]
        visited = set()
        def dfs(i):
            if i in visited:
                return
            visited.add(i)
            for child in adjls.get(i, []):
                dfs(child)

        result = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                result += 1
        return result

if __name__ == "__main__":
    inputs = [
        (5, [[0,1],[1,2],[3,4]], 2),
        (5, [[0,1],[1,2],[2,3],[3,4]], 1)
    ]
    for n, edges, expected in inputs:
        print(Solution.naive(n, edges))