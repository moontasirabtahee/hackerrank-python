n = int(input())
dic = {}
for i in range(n):

    name,math,phy,che = input().split()
    score= map(float,[math,phy,che])

    dic[name]= score
nagin = input()
avg=sum(dic[nagin])/3
print("%.2f"%avg)