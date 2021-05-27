#euler24
import itertools
nums = [0,1,2,3,4,5,6,7,8,9]
perm = itertools.permutations(nums)
print(list(perm)[999999])
