n,m = map(int, input().split())
arr = [0]*n
for _ in range(m):
    a,b,c = map(int, input().split())
    for j in range(a, b+1):
        arr[j-1] = c
print(" ".join(map(str, arr)))