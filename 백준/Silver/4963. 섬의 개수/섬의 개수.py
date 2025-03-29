from collections import deque
def bfs(x,y):
    q = deque()
    q.append([x,y])
    dx = [-1,-1,-1, 0, 0, 1, 1, 1]  
    dy = [-1, 0, 1,-1, 1,-1, 0, 1]
    graph[x][y]=0
    while q:
        n,m = q.popleft()
        for i in range(8):
            X,Y = dx[i]+n, dy[i]+m
            if 0<=X<b and 0<=Y<a and graph[X][Y]==1:
                graph[X][Y]=0
                q.append([X,Y])
            

while True:
    a,b = map(int, input().split())
    cnt = 0
    if a==b==0:
        break
    graph = []
    for _ in range(b):
        graph.append(list(map(int, input().split())))
    for i in range(b):
        for j in range(a):
            if graph[i][j]==1:
                bfs(i,j)
                cnt+=1
    print(cnt)