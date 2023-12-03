testcases = [
    (7, [5, 3, 4, 7]),
    (7, [2, 1]),
    (7, [5, 3, 4, 1]),
    (1, [2, 5])
]

# bottom up
def recur(target, coins):
    if target == 0:
        return []
    if target < 0:
        return None
    
    minLength = float('inf')
    cur = None
    for i, coin in enumerate(coins):
        tmp = recur(target-coin, coins)
        if isinstance(tmp, list):
            tmp = tmp + [coin]
            L = len(tmp)
            if L < minLength:
                minLength = L
                cur = tmp
    return cur

# up bottom
class Solution:
    def __init__(self):
        self.res = None
        self.minLength = float('inf')

    def __call__(self, target, coins, hist):
        if target < 0:
            return
        
        if target == 0:
            L = len(hist)
            if L<self.minLength:
                self.minLength = L
                self.res = hist
        
        for coin in coins:
            self.__call__(target-coin, 
                coins, hist+[coin])

def recur2(target, coins, hist):
    if target < 0: 
        return None
    if target == 0:
        return hist
    
    minLength = float('inf')
    cur = None
    for coin in coins:
        newhist = recur2(target-coin, coins, hist+[coin])
        if isinstance(newhist, list):
            L = len(newhist)
            if L < minLength:
                minLength = L
                cur = newhist
    return cur


for target, coins in testcases:
    print("---------------------")
    print(recur(target, coins))

    soln = Solution()
    soln(target, coins, [])
    print(soln.res, soln.minLength)

    print(recur2(target, coins, []))