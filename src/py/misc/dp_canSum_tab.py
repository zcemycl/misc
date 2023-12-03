testcases = [
    (7, [5, 3, 4, 7]),
    (1, [2, 5])
]

class Solution:
    def __init__(self, coins):
        self.reset(coins)
    
    def reset(self, coins):
        self.coins = coins
    
    def __call__(self, target):
        arr = [False]*(target+1)
        arr[0] = True
        for i in range(1, target+1):
            for coin in self.coins:
                prev = i-coin
                if prev < 0:
                    continue
                elif prev >= 0:
                    if arr[prev]:
                        arr[i] = arr[prev]
                        break
        print(arr)
        return arr[-1]



for target, coins in testcases:
    soln = Solution(coins)
    print(soln(target))