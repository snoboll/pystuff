def has_one(s, c):
    if s.count(str(c)) == 1:
        return True
    else:
        return False

res = set()
for a in range(10000):
    if '0' not in str(a):
        for b in range(10000):
            if '0' not in str(b):
                prod = a * b
                if prod > 100000:
                    break
                else:
                    check = str(a) + str(b) + str(prod)
                    valid = True
                    for i in range(1, 10):
                        if not has_one(check, i):
                            valid = False
                    if valid and len(check) == 9:
                        print(a, b, prod)
                        res.add(prod)
            
print(sum(res))