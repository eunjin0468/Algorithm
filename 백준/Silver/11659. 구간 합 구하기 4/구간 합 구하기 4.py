import sys
input = sys.stdin.readline

n,m = map(int, input().split())
arr = list(map(int, input().split()))
sum = [0]
tmp = 0
for i in arr:
    tmp += i
    sum.append(tmp)

for _ in range(m):
    a,b = map(int, input().split())
    print(sum[b]-sum[a-1])