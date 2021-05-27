#euler25
def fib():
    fiblist = [0,1]
    while(True):
        nextfib = fiblist[-1] + fiblist[-2]
        fiblist.append(nextfib)
        if len(str(nextfib)) > 999:
            break
    return len(fiblist)-1

print(fib())
