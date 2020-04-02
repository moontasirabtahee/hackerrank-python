def swap(N):
    new = ""
    for i in N:
        if i.isupper()==True:
           new+=i.lower()
        else:
            new+=i.upper()
    return new

N = input()
print(swap(N))
