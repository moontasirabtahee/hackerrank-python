def print_formatted(number):
    w = len(bin(n).replace("0b",''))
    for i in range(1,n+1):
        he=hex(i).replace("0x",'').upper()
        oc=oct(i).replace('0o','')
        bi = bin(i).replace('0b','')
        de=str(i)

        print(de.rjust(w),oc.rjust(w),he.rjust(w),bi.rjust(w))



if __name__ == '__main__':
    n = int(input())
    print_formatted(n)