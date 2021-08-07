from math import factorial

def n_over_k(n, k):
    return (factorial(n)/ (factorial(n-k) * factorial(k)))

print(n_over_k(40, 20))