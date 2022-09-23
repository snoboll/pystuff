from locale import currency
from multiprocessing.dummy import current_process
import helpers

limit = 1000
primes = []

for i in range(limit):
    if (helpers.is_prime(i)):
        primes.append(i)

current = 0
window_size = limit
loop_count = 0

while True:
    current = 0
    for _ in range(len(primes) - loop_count):
        ans = sum(primes[current:current+window_size])
        if (ans in primes):
            print(ans, current, window_size)
            print(primes[current:current+window_size])
            exit()
        current += 1
    else:
        window_size -= 1
        loop_count += 1
        print(loop_count)
