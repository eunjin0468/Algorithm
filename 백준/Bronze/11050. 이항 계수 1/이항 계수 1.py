from itertools import combinations
a,b=map(int, input().split())
arr = [i for i in range(a)]
print(len(list(combinations(arr, b))))