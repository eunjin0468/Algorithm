import sys
sys.setrecursionlimit(10 ** 8)

t = int(input())
def dfs(y,x):
    global cnt
    visited[y][x]=1
    for dy,dx in d:
        Y,X = y+dy, x+dx
        if 0<=Y<n and 0<=X<n and visited[Y][X]==0 and arr[Y][X]=='-':
            cnt+=1
            dfs(Y,X)
for _ in range(t):
    n = int(input())
    arr = [list(input()) for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    d = [(0,0),(0,-1),(0,1),(-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1)]
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j]=='w' and visited[i][j]==0:
                dfs(i,j)
    print(cnt)