from itertools import combinations_with_replacement
n,m = map(int, input().split())
arr = list((map(int, input().split())))
arr.sort()
ans = combinations_with_replacement(arr, m)
for a in ans:
    print(*a)