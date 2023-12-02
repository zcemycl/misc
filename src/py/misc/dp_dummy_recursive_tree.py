def recur(n):
    print(n)
    # termination criteria
    if n==3:
        return
    # recursive call
    recur(n+1)
    recur(n+1)

recur(0)
