from itertools import combinations
n,m = map(int, input().split())
arr = [i for i in range(1, n+1)]
ans = combinations(arr,m)
for a in ans:
    print(*a)