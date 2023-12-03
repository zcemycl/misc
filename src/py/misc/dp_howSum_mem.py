testcases = [
    (7, [5, 3, 4, 7]),
    (7, [1, 2]),
    (1, [2, 5])
]

class Solution:
    def __init__(self, coins):
        self.reset(coins)

    def reset(self, coins):
        self.coins = coins
        self.hist = {}

    def __call__(self, target):
        if target == 0:
            return []
        if target in self.hist:
            return self.hist[target]
        if target < 0:
            return None

        for coin in self.coins:
            tmp = self.__call__(target-coin)
            self.hist[target-coin] = tmp
            if isinstance(tmp, list):
                self.hist[target-coin] = tmp.copy()
                tmp.append(coin)
                return tmp

for target, coins in testcases:
    soln = Solution(coins)
    print(soln(target))
    print(soln.hist)