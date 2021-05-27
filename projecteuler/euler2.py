#problem2

summa = 0

c = 0
a = 1
b = 2

while c < 4000000:
    c = a+b
    if c % 2 == 0:
        summa = summa + c

    a = b
    b = c        

print (summa+2)
