testcases = [
    (7, [5, 3, 4, 7]),
    (1, [2, 5])
]

def recur(coins, target):
    if target == 0:
        return True
    if target < 0:
        return False
    
    for coin in coins:
        isTrue = recur(coins, target-coin)
        if isTrue: return isTrue
    
    return False

for target, coins in testcases:
    print(recur(coins, target))