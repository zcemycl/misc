class Solution:
    @classmethod
    def naive_solution(cls, coins, amount):
        if amount == 0:
            return 0
        cls.result = 10**5
        L = len(coins)
        visited = {}
        def dfs(i, count, left, members):
            if i==L: return
            if left == coins[i]:
                print(members+[coins[i]], count+1)
                cls.result = min(cls.result, count+1)
                return
            newleft = left-coins[i]
            if newleft < 0:
                return
            # choose and stay the same coin, 
            dfs(i, count+1, newleft, members+[coins[i]])
            # skip this
            dfs(i+1, count, left, members)
        dfs(0, 0, amount, [])
        return cls.result if cls.result!=10**5 else -1

    @classmethod
    def dp(cls, coins, amount):
        if amount == 0:
            return 0
        dps = [amount+1 for i in range(amount+1)]
        dps[0] = 0
        for i in range(1, amount+1):
            if i in coins:
                dps[i] = 1
            else:
                for c in coins:
                    if c > i or i < c:
                        continue
                    dps[i] = min(dps[i], 1+dps[i-c])
        print(dps)
        return dps[-1] if dps[-1]!=amount+1 else -1

if __name__ == "__main__":
    inputs = [
        ([1,2,5],11,3),
        ([2],3,-1),
        ([1],0,0),
        ([2,5,10],25,3),
        ([3,7,405,436],8839,25)
    ]
    for coins, amount, result in inputs:
        # print(Solution.naive_solution(coins, amount))
        print(Solution.dp(coins, amount))