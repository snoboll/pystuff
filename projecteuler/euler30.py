#euler30
sum = 0
for num in range(1000000):
    snum = str(num)
    numsum = 0
    for j in snum:
        k = int(j)
        numsum += k**5
    if numsum == num:
        sum += num
        print(num)
print(sum-1)
