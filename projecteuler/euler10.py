import time
from helpers import is_prime

start_time = time.time()
sum = 0
for num in range(2, 2000000):
    if is_prime(num):
        sum += num

print(sum, '  --- time:', (time.time() - start_time), 's ---')