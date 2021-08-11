from numpy.core.fromnumeric import prod
import numpy as np

def get_max(mat):
    biggest = 0
    for row in mat:
        i = 0
        while i < 17:
            window = row[i:i+4]
            p = prod(window)

            if p > biggest:
                biggest = p
            
            i += 1

    return biggest

def get_diag_max(mat):
    biggest = 0
    for i in range(17):
        for j in range(17):
            window = [mat[i][j], mat[i + 1][j + 1] , mat[i + 2][j + 2], mat[i + 3][j + 3]]

            p = prod(window)
            if p > biggest:
                biggest = p

    for i in range(17):
        for j in range(19, 2, -1):
            window = [mat[i][j], mat[i + 1][j - 1] , mat[i + 2][j - 2], mat[i + 3][j - 3]]
            p = prod(window)

            if p > biggest:
                biggest = p
    return biggest

# parsing
with open('euler11input.txt', 'r') as f:
    f_contents = f.readlines()

f_contents = [l.strip() for l in f_contents]

mat = []
for l in f_contents:
    m = [int(a) for a in l.split(' ')]
    mat.append(m)

# horizontally
hor = get_max(mat)

# vertically
mat_transpose = np.array(mat).transpose()
vert = get_max(mat_transpose)

# diagonally
diag = get_diag_max(mat)


print(hor, vert, diag)