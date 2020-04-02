
from array import *
n = int(input())
ar =[]
score=[]
name=[]
for i in range(n):
    #ar=[[input(),float(input())]]
    x = input()
    y = float(input())
    score.append(y)
    ar.append([x,y])


p=sorted(score)

q =min(score)
s=0
for i in range(len(score)):
    if p[i]!= q:
        s=p[i]
        break
for x,y in ar:
    if y==s:
        name.append(x)
name.sort()
for nam in name:
    print(nam, end="\n")