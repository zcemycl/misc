class Solution:
    @classmethod 
    def naive(cls, numCourses, prerequisites):
        cls.adjls = {}
        for take, require in prerequisites:
            cls.adjls[take] = cls.adjls.get(take, []) + [require]
        print(cls.adjls)
        cls.cache = {}
        def dfs(i, visited):
            if len(cls.adjls.get(i, [])) == 0:
                print(visited|set([i]))
                cls.cache[i] = True
                return True
            if i in visited:
                return False
            if i in cls.cache:
                print(visited|set([i]))
                return cls.cache[i]
            for child in cls.adjls[i]:
                isFinish = dfs(child, visited|set([i]))
                cls.cache[child] = isFinish
                if not isFinish:
                    return False
            return True

        for i in range(numCourses):
            isFinish = dfs(i, set())
            cls.cache[i] = isFinish
            if not isFinish:
                return False
        print(cls.cache)
        return True

if __name__ == "__main__":
    inputs = [
        (2, [[1,0]], True),
        (2, [[1,0],[0,1]], False),
        (6, [[5,4],[5,3],[3,1],[4,2],[1,0],[2,0]], True),
        (7, [[1,4],[3,4],[5,6],[5,1],[2,1],[2,3],[0,5],[0,2]], True),
        (7, [[1,4],[3,4],[5,6],[5,1],[2,1],[2,3],[0,5],[2,0]], True),
        (4, [[5,1],[1,2],[2,0],[0,5]], False),
    ]
    for numCourses, prerequisites, expected in inputs:
        print(Solution.naive(numCourses,prerequisites))
        print("------")


