testcases = [
    (7, [1, 2]),
    (1, [2, 5])
]

class Solution:
    def __init__(self, coins):
        self.reset(coins)
    
    def reset(self, coins):
        self.hist = {}
        self.coins = coins
    
    def __call__(self, target):
        if target == 0:
            return True
        if target in self.hist:
            return self.hist[target]
        if target < 0:
            return False
        
        for coin in self.coins:
            isPossible = self.__call__(target-coin)
            self.hist[target-coin] = isPossible
            if isPossible:
                return isPossible
        return False


for target, coins in testcases:
    soln = Solution(coins)
    print(soln(target))
    print(soln.hist)