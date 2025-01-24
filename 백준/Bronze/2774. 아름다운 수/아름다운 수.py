t = int(input())
for _ in range(t):
    num = input()
    dic = {}
    for n in num:
        if int(n) in dic:
            dic[int(n)] += 1
        else:
            dic[int(n)] = 1
    print(len(dic))