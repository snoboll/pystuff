import time
from helpers import is_prime

if __name__ == '__main__':
    start_time = time.time()
    sum = 0
    for num in range(2, 2000000):
        if is_prime(num):
            sum += num

    print('Ans:', sum, '   Time:', time.time()/1000, 'ms')