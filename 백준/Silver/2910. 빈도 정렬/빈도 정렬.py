n,c = map(int, input().split())
arr = list(map(int, input().split()))
dic = {}
 
for a in arr:
    if a in dic:
        dic[a] += 1
    else:
        dic[a] = 1
dicc= sorted(dic.items(), key=lambda x:x[1], reverse=True)
 
for a,b in dicc:
    while b>0:
        print(a, end=' ')
        b-=1