n,m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
num = [0]*(n+1)
for a,b in arr:
    for i in range(a, n+1, b):
        num[i] = 1
print(num.count(0)-1)