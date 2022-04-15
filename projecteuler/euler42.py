

def get_word_val(s):
    ret = 0
    for c in s:
        ret += ord(c) - 64
    return ret

def get_tri_nums(n):
    ret = set()
    for i in range(n):
        ret.add(int(i*(i+1)/2))
    
    print(ret)
    return ret

if __name__ == '__main__':
    
    with open('euler42input.txt') as f:
        lines = f.read().split(",")

    triset = get_tri_nums(20)

    triwordcount = 0
    for word in lines:
        word = word.strip("\"")
        val = get_word_val(word)
        if val in triset:
            # print(val, word)
            triwordcount += 1
    
    print(triwordcount)