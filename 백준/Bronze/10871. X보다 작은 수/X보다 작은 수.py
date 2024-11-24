import sys
a, b = map(int, input().split())
arr = list(map(int, input().split()))
result = []
for i in arr:
    if i < b:
        result.append(i)
print(' '.join(map(str, result)))
