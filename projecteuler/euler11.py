with open('euler11input.txt', 'r') as f:
    f_contents = f.readlines()

f_contents = [l.strip() for l in f_contents]

mat = []
for l in f_contents:
    for n in l.split(' '):
        print(n)

# print(f_contents)