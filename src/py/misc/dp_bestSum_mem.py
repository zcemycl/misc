testcases = [
    (7, [5, 3, 4, 7]),
    (7, [2, 1]),
    (7, [5, 3, 4, 1]),
    (1, [2, 5]),
    (100, [1, 2, 25])
]

class Solution:
    def __init__(self, coins):
        self.coins = coins
        self.reset()
       
    def reset(self):
        self.hist = {}
        self.res = None
        self.minLength = float('inf')

    def recur(self, target):
        if target == 0:
            return []
        if target in self.hist:
            return self.hist[target]
        if target < 0:
            return None

        minLength = float('inf')
        cur = None
        for coin in coins:
            tmp = self.recur(target-coin)
            
            if tmp == None:
                continue
            if isinstance(tmp, list):
                L = len(tmp)
                if target-coin in self.hist:
                    if L < len(self.hist[target-coin]):
                        self.hist[target-coin] = tmp
                else:
                    self.hist[target-coin] = tmp
                tmp = tmp + [coin]
                if L+1 < minLength:
                    minLength = L+1
                    cur = tmp
        return cur

    def recur2(self, target):
        if target in self.hist:
            return self.hist[target]
        if target < 0:
            return None

        



for target, coins in testcases:
    print("---------------------")
    soln = Solution(coins)
    print(soln.recur(target))

    # soln = Solution()
    # soln(target, coins, [])
    # print(soln.res, soln.minLength)

    # print(recur2(target, coins, []))