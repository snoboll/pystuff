from itertools import permutations

nums = [0,1,2,3,4,5,6,7,8,9]
perm = permutations(nums)

print(list(perm)[999999])