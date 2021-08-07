import time

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

if __name__ == '__main__':
    start_time = time.time()
    sum = 0
    for num in range(2, 2000000):
        if is_prime(num):
            sum+=num

    print('Ans:', sum, '   Time:', time.time()/1000, 'ms')
