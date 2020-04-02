from itertools import *
N,a=input().split()
N= sorted(N)

l=list(combinations_with_replacement(N,int(a)))

for i in l:
    print(''.join(i))