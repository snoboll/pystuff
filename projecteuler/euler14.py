import time

def euler14():
    ans = 0
    seq_length = 0

    cache = {0:-1, 1:1}

    for i in range(2, 1000000):

        n = i
        count = 0
        while n != 1:
            count += 1
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1

        cache[i] = count + cache[int(n)]

        if cache[i] > seq_length:
            seq_length = cache[i]
            ans = i

    return ans

time1 = time.time()
print(euler14(), 'Time:', time.time() - time1)