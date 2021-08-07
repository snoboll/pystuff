from collections import deque
from euler10 import is_prime

def dq_to_int(dq):
    ret = ''
    for e in dq:
        ret += str(e)
    return int(ret)

circ_primes = []
for num in range(2, 1000000):
    digit_string = str(num)
    digit_map = map(int, digit_string)
    digit_list = list(digit_map)
    dq = deque(digit_list)

    # print(dq)

    is_circ_prime = True
    while is_circ_prime:
        for _ in range(len(dq)):
            if not is_prime(dq_to_int(dq)):
                is_circ_prime = False
                break
            
            dq.rotate()

        if is_circ_prime:
            circ_primes.append(num)
            print(num)
            is_circ_prime = False

print(len(circ_primes))