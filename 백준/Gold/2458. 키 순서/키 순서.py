import sys
max = 9999
n,m = map(int, sys.stdin.readline().split())
height = [[max for _ in range(n+1)] for _ in range(n+1)]
for i in range(m):
    tall, small = map(int, sys.stdin.readline().split())
    height[tall][small] = 1
    
for i in range(1, n+1): #가운데 노드
    for j in range(1, n+1): #시작 노드
        for k in range(1, n+1): #마지막 노드
            if height[j][k] > height[j][i] + height[i][k]:
                height[j][k] = height[j][i] + height[i][k]

result = 0
for i in range(1, n+1):
    cnt = 0
    for j in range(1, n+1):
        if height[i][j]!=max or height[j][i]!=max:
            cnt+=1
    if cnt == n-1:
        result+=1
print(result)