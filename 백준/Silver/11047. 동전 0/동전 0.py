n,k = map(int,input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
result = 0
for coin in arr:
    if k >= coin:
        result += k//coin
        k%=coin
    if k<=0:
        break
print(result)