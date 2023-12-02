def fib(n, hist) -> tuple[int, dict[int, int]]:
    if n in hist: return hist[n], hist
    if n<=2: return 1, hist
    n1, hist = fib(n-1, hist)
    hist[n-1] = n1
    n2, hist = fib(n-2, hist)
    hist[n-2] = n2
    return n1+n2, hist

print(fib(1, {}))
print(fib(5, {}))
print(fib(8, {}))