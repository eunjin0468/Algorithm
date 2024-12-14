n = int(input())
dic = {}
for _ in range(n):
    file = input().split('.')[1]
    if file not in dic:
        dic[file] = 1
    else:
        dic[file]+=1
dict = sorted(dic.items(), key=lambda x:x[0])
for i in range(len(dict)):
    print(dict[i][0], dict[i][1])