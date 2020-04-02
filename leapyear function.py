#N= int(input())
#if (N%4==0 and N%100 !=0) or (N%400==0 and N%100 !=0:)
    #print(True)

#else:
    #print(False)
#def check(N):
#    if N%4==0 and N%100!=0 and N%400==0:
#        leap = True
#    else:
#        leap =False
#    return leap
#print(check(N))
def is_leap(year):
    leap = False
    if year%4==0:
        if year%100!=0 or year%400==0:
            leap = True

    return leap


year = int(input())
print(is_leap(year))



