def fib_index(n):
    fiblist = [0, 1]
    while(True):
        nextfib = fiblist[-1] + fiblist[-2]
        fiblist.append(nextfib)
        if len(str(nextfib)) > n:
            return len(fiblist) - 1

print(fib_index(999))