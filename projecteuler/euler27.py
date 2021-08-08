from helpers import is_prime

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
        output = n ** 2 + a * n + b
        while(is_prime(output)):
            n += 1
            conscount += 1
            output = n ** 2 + a * n + b
            if conscount > bestcount:
                bestcount = conscount
                besta = a
                bestb = b
                prod = a * b

print(besta, bestb, prod)