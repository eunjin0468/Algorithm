n = int(input())
arr = list(map(int, input().split()))
num = sorted(set(arr))
dic = {num[i]:i for i in range(len(num))}
for i in arr:
    print(dic[i], end=' ')