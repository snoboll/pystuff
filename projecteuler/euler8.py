from numpy.core.fromnumeric import prod

with open('euler8input.txt', 'r') as f:
	f_contents = f.readlines()

s_num = ''.join([s.strip() for s in f_contents])
digit_list = list(map(int, s_num))

window = digit_list[0:13]
ans = prod(window)

i = 0
while i + 13 < 1000:
    window = digit_list[i: i + 13]
    p = prod(window)
    
    if p > ans:
        ans = p

    i += 1

print(ans)