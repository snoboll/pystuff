def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n % 3 == 0 or n == 1:
        return False
    
    i = 5
    while i ** 2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def get_prime_factors(n):
    d = 2
    prime_factors = []
    while d < n:
        while n % d == 0 and is_prime(d):
            print(n, d)
            n /= d
            prime_factors.append(d)
        d += 1

    prime_factors.append(int(n))
    return prime_factors


def is_palindrome(s):
    if s[0] == '0' or s[-1] == '0':
        return False

    i = 0
    ii = len(s)-1
    while s[i] == s[ii]:
        i += 1
        ii -= 1
        
        if i >= len(s) / 2:
            return True

    return False
