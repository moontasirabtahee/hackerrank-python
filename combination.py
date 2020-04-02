from itertools import *
N,A =input().split()
N= sorted(N)
p=[]
l=[]
for i in range(1,int(A)+1):
    l += list(combinations(N,i))


for x in l:
    print(''.join(list(x)))