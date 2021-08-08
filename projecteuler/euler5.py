from helpers import get_prime_factors

print(5 * 2 * 2 * 19 * 3 * 17 * 2 * 2 * 7 * 13 * 11 * 3)

ans = 1
for i in range(21):
    for p in get_prime_factors(i):