testcases = [
    (7, [5, 3, 4, 7]),
    (7, [1, 2]),
    (1, [2, 5])
]

def recur(target, coins):
    if target == 0:
        return []
    if target < 0:
        return None

    for coin in coins:
        tmp = recur(target-coin, coins)
        if isinstance(tmp,list):
            tmp.append(coin)
            return tmp

    return None

for target, coins in testcases:
    print(recur(target, coins))