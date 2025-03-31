from collections import deque
y,x = map(int, input().split())
graph = []
cnt = 0
for i in range(y):
    graph.append(list(map(int, input().split())))
    cnt+=sum(graph[i])
dx = [0,0,-1,1]
dy = [-1,1,0,0]
time = 1

def bfs():
    q = deque([(0,0)])
    melt = deque([])
    while q:
        a,b = q.popleft()
        for i in range(4):
            ny, nx = a+dy[i], b+dx[i]
            if 0<=ny<y and 0<=nx<x and visited[ny][nx]==0:
                visited[ny][nx]=1
                if graph[ny][nx]==1: #치즈면 한 번에 녹임
                    melt.append((ny, nx))
                elif graph[ny][nx]==0: #공기면 계속 탐색
                    q.append((ny, nx))
    for j,k in melt:
        graph[j][k] = 0
    return len(melt)

while 1:
    visited = [[0]*x for _ in range(y)]
    melCnt = bfs()
    cnt-=melCnt
    if cnt==0: #치즈가 다 녹았으면
        print(time, melCnt, sep='\n')
        break
    time+=1