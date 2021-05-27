#euler 28
#1002001
i = 1
add = 2
count4 = 0
sum = 0
while i < 1002001:
    i += add
    print(i)
    sum += i
    count4 += 1
    if count4 == 4:
        add += 2
        count4 = 0

sum += 1
print(sum)
