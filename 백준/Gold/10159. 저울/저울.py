import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
graph = [[0]*n for _ in range(n)]

for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1
    
for i in range(n): #가운데 노드
    for j in range(n): #시작 노드
        for k in range(n): #마지막 노드
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
                
for i in range(n):
    cnt = 0
    for j in range(n):
        if not graph[i][j] and not graph[j][i]:
            cnt+=1
    print(cnt-1) #자기자신 제외