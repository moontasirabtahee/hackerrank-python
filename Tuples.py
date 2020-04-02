n = int(input())
#x= list(map(int,input().split()))\
x = input().split()
x=map(int,x)

t = tuple(x)

print (hash(t))
