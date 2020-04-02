list =[]
def insert(x,y):
    list.insert(x,y)

def remove(e):
    list.remove(e)

def append(e):
    list.append(e)

def sort():
    list.sort()

def pop():
    list.pop()

def reverse():
    list.reverse()


N = int(input())

for counter in range(N):
    q,*p = input().split()
    if q=="insert":
        #p = map(int,p)
        insert(int(p[0]),int(p[1]))
    elif q == 'print':
        print(list)
    elif q == "remove":
       #p = map(int, p)
        remove(int(p[0]))

    elif q =='append':
        #p = map(int, p)
        append(int(p[0]))
    elif q == 'sort':
        sort()
    elif q == 'pop':
        pop()

    elif q == "reverse":
        reverse()
