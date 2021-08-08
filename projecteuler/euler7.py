from helpers import is_prime

count = 0
n = 1

while count < 10001:
    n += 1
    if is_prime(n):
        count += 1

print(n)