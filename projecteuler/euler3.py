from euler10 import is_prime
import math

bignum = 600851475143

for d in range(math.floor(math.sqrt(bignum)), 0, -1):
    if is_prime(d) and bignum % d == 0:
        print(d)
        break