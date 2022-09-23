def penta(n):
    return n * (3 * n - 1) / 2
    

def get_penta_list(n):
    ret = []
    for i in range(n):
        ret.add(penta(i))

    return ret


if __name__ == "__main__":
    penta_list = get_penta_list(100000)
    pentaset = set(penta_list)

    d = 10000000
    i, j = 0, 0

    while True:
        not (penta_list[i] + penta_list[j] in pentaset and abs(penta_list[i] - penta_list[j]) in pentaset):
        if i == len(penta_list):
            i = 0
            j += 1
        else:
            i += 1

        if abs(pentalist[i] - penta_list[j]) < d:
                d = diff
                ans = (pj, pk)

    print(mindiff, ans)

