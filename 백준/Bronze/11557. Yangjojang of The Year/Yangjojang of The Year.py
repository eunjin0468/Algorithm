n = int(input())
for _ in range(n):
    m = int(input())
    dic = {}
    for i in range(m):
        a,b = input().split()
        dic[a] = {'alcohol': int(b)}
    sorted_dic = sorted(dic.items(), key=lambda x:x[1]['alcohol'])
    print(sorted_dic[-1][0])