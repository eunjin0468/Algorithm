import math

n = int(input())
arr = list(map(int, input().split()))
b,c = map(int, input().split())

ans = n

for a in arr:
    a -= b
    if a>0:
       ans += math.ceil(a / c) 
print(ans)