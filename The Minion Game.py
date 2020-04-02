S = input().upper()
w = "AEIOU"
k,s=0,0
for i in range(len(S)):
    if S[i] in w:
        k+=len(S)-i
    else:
        s+=len(S)-i

if k > s:
    print('Kevin',k)
elif s==k:
    print('Draw')

else:
    print("Stuart",s)