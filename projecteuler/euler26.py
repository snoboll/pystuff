#euler26
from decimal import *
getcontext().prec += 10

a = []
for i in range(1, 1000):
    a.append(1/i)

print(a)
