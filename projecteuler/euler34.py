import math

curious = []

for num in range(10000000):
    sum = 0
    digit_string = str(num)
    digit_map = map(int, digit_string)
    digit_list = list(digit_map)

    # print(digit_list)
    fac_sum = 0
    for i in digit_list:
        fac_sum += math.factorial(i)
    
    if fac_sum == num:
        curious.append(num)

print(curious)
print(sum(curious)-3)