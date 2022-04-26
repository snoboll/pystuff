import math, time

def penta(n):
    return int(n * (3*n-1)/2)

def hexa(n):
    return int(n * (2*n - 1))


def is_penta(n):
    for i in range(int(math.sqrt(n)*2)):
        if penta(i) == n:
            return True
    return False

def is_hexa(n):
    for i in range(int(math.sqrt(n)*2)):
        if hexa(i) == n:
            return True
    return False


def sol():
    # tn, pn, hn = 285, 165, 143
    hn = 143
    ans = hexa(hn)

    while True:
        hn += 1
        ans = hexa(hn)
        if ans % 1000 == 0:
            print(ans)
        if is_penta(ans):
            print(ans)
            break

if __name__ == "__main__":
    start = time.time()
    sol()    
    end = time.time()
    print("Time elapsed: " + str(end - start))

