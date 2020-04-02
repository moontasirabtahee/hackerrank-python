from itertools import groupby
N = input()
N=sorted(N)
#for i ,j in groupby(N):
    #print((len(list(j)),int(i)),end=" ")
print(list(groupby(N)))