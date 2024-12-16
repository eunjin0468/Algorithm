import sys
n,l = map(int, sys.stdin.readline().split())
graph = [[0]*n for _ in range(n)]

for _ in range(l):
    x,y = map(int, sys.stdin.readline().split())
    graph[x-1][y-1] = 1

for i in range(n): #가운데 노드
    for j in range(n): #시작 노드
        for k in range(n): #마지막 노드
            if graph[j][i] and graph[i][k]:
                graph[j][k] = 1
    
s = int(sys.stdin.readline())

for _ in range(s):
    x,y = map(int, sys.stdin.readline().split())
    if graph[x-1][y-1]==1:
        print(-1)
    elif graph[y-1][x-1]==1:
        print(1)
    else:
        print(0)