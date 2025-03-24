from collections import deque
import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [1,-1,0,0,0,0]
dy = [0,0,-1,1,0,0]
dz = [0,0,0,0,-1,1]

def bfs(x,y,z):
    q.append([x,y,z])
    visited[x][y][z] = 1 #방문표시
    while q:
        x,y,z = q.popleft()
        for i in range(6):
            nx = x+dx[i]
            ny = y+dy[i]
            nz = z+dz[i]
            if 0<=nx<l and 0<=ny<r and 0<=nz<c:
                if graph[nx][ny][nz]=='E':
                    print("Escaped in {0} minute(s).".format(visited[x][y][z]))
                    return
                if graph[nx][ny][nz]=='.' and visited[nx][ny][nz]==0:
                    visited[nx][ny][nz] = visited[x][y][z]+1
                    q.append([nx,ny,nz])
    print('Trapped!')

while 1:
    l,r,c = map(int, input().split())
    if l==r==c==0:
        break
    graph = [[[]*c for _ in range(r)] for _ in range(l)]
    visited = [[[0]*c for _ in range(r)] for _ in range(l)] #방문기록
    q=deque()

    for i in range(l):
        graph[i] = [list(map(str, input().strip())) for _ in range(r)]
        input()
    
    for i in range(l):
        for j in range(r):
            for k in range(c):
                if graph[i][j][k] == 'S':
                    bfs(i, j, k)