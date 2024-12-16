import sys
INF = int(1e9)
n = int(sys.stdin.readline()) #도시의 개수
m = int(sys.stdin.readline()) #버스의 개수
graph = [[INF]*(n+1) for _ in range(n+1)]
for i in range(1, n+1): #출발지역=도착지역 
    for j in range(1, n+1):
        if i==j:
            graph[i][j] = 0
for _ in range(m): #최단거리 입력
    a, b, c = map(int, sys.stdin.readline().split())
    graph[a][b] = min(c, graph[a][b])
for i in range(1, n+1): #가운데 노드
    for j in range(1, n+1): #시작 노드
        for k in range(1, n+1): #마지막 노드
            graph[j][k] = min(graph[j][k], graph[j][i]+graph[i][k])
for i in range(1, n+1):
    for j in range(1, n+1):
        if graph[i][j] == INF:
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()