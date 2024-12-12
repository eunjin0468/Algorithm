from queue import deque
def bfs(i, j):
    queue = deque()
    queue.append((i,j))
    
    while queue:
        i,j = queue.popleft()
        
        for k in range(4):
            nx = i+dx[k]
            ny = j+dy[k]
            
            if nx<0 or nx>=n or ny<0 or ny>=m:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[i][j]+1
                queue.append((nx, ny))
    return(graph[n-1][m-1])

n,m = map(int, input().split())
graph = []
result = 0

for i in range(n):
    graph.append(list(map(int, input())))
            
dx = [-1,1,0,0]
dy = [0,0,-1,1]

print(bfs(0,0))