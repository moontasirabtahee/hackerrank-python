from textwrap import *
s = input()
k = int(input())
l = wrap(s,k)
print(l)
for i in range(len(l)):
    l[i]=''.join(list(dict.fromkeys(l[i])))

for i in range(len(l)):
    print(l[i])