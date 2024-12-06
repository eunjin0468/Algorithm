n = int(input())
dic={}
for _ in range(n):
    a,b,c,d = input().split()
    dic[a] = {'day': int(b), 'month': int(c), 'year':int(d)}
sorted_dic = sorted(dic.items(), key=lambda x: (x[1]['year'], x[1]['month'], x[1]['day']))
print(sorted_dic[-1][0])
print(sorted_dic[0][0])