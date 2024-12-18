a,b = map(int, input().split())
dic = {}
for i in range(1,a+1):
    dic[i] = i
for i in range(1, b+1):
    c,d = map(int, input().split())
    tmp = dic[c]
    dic[c] = dic[d]
    dic[d] = tmp
for i in dic:
    print(dic[i], end = ' ')