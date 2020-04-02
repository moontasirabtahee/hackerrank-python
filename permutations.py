from itertools import permutations
A ,b=input().split()
A =sorted(A)
x=(list(permutations(A,int(b))))
for i in x:
    print(''.join(i))