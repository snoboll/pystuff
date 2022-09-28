from decimal import *

getcontext().prec = 1000

ans = 1
decimal_string = ""

for i in range(1, 1000):
    q = Decimal(1)/Decimal(i)
    for c in str(q)[2:]:
        decimal_string += c
    
    for j in range(len(decimal_string)):
        word = decimal_string[0:len(decimal_string)-1-j]
        max_found = len(word)
        if decimal_string.count(word) > 1 and max_found > ans:
            ans = max_found
            print(i)
            print(decimal_string)

    decimal_string = ""
print(ans)


