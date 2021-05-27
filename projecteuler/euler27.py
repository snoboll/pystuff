#euler27
def isPrime(n):
    if (n <= 1) :
        return False
    if (n <= 3) :
        return True
    if (n % 2 == 0 or n % 3 == 0) :
        return False

    i = 5
    while(i * i <= n) :
        if (n % i == 0 or n % (i + 2) == 0) :
            return False
        i = i + 6

    return True

a = 1
b = 1
bestcount = 0
besta = a
bestb = b

for a in range(-999, 1000):
    print(a)
    for b in range(-1000, 1001):
        conscount = 0
        n = 0
        output = n**2 + a*n + b
        while(isPrime(output)):
            n += 1
            conscount += 1
            output = n**2 + a*n + b
            if conscount > bestcount:
                bestcount = conscount
                besta = a
                bestb = b
                prod = a*b

print(besta, bestb, prod)
