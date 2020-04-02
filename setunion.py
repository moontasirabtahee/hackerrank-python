from math import *
A=int(input())
a=set(map(int, input().split()))
A2= int(input())
b=set(map(int, input().split()))

t=a.symmetric_difference(b)
print(len(t))

