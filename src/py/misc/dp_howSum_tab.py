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
        arr = [[]]*(target+1)

        for i in range(1, target+1):
            for coin in self.coins:
                tmp = i-coin
                if tmp > 0:
                    tmpls = arr[tmp].copy()
                    if len(tmpls)!=0:
                        tmpls.append(coin)
                        arr[i] = tmpls
                        break
                elif tmp == 0:
                    tmpls = arr[tmp].copy()
                    tmpls.append(coin)
                    arr[i] = tmpls
                    break
        
        print(arr)
        return arr[-1]

for target, coins in testcases:
    soln = Solution(coins)
    print("Answer: ", soln(target))
                