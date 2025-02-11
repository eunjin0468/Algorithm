import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n,m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
visited = [[0]*m for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
sheep, wolve = 0,0
a,b = 0,0

def in_range(i,j):
    return 0<=i<n and 0<=j<m

def dfs(i,j):
    global a,b
    if in_range(i,j):
        if arr[i][j]!='#' and visited[i][j] == 0:
            visited[i][j] = True
            if arr[i][j] =='o':
                a+=1
            elif arr[i][j] == 'v':
                b+=1
            for k in range(4):
                nx = dx[k]+i
                ny = dy[k]+j
                dfs(nx, ny)
            return True
        return False

for i in range(n):
    for j in range(m):
        a,b = 0,0
        if dfs(i,j) == True:
            if a>b:
                sheep+=a
            else:
                wolve+=b
print(sheep, wolve)