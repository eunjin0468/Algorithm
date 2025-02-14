import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
arr = [list(input()) for _ in range(n)]
dx = [0,0,-1,1]
dy = [-1,1,0,0]
a,b = 0,0

def dfs(i,j):
    visited[i][j] = 1
    color = arr[i][j]
    for k in range(4):
        x,y = dx[k]+i, dy[k]+j
        if 0<=x<n and 0<=y<n and visited[x][y] == 0 and arr[x][y]==color:
            dfs(x,y)

visited = [[0]*(n) for _ in range(n)] #일반인용
for i in range(n): #일반인
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            a+=1
            
visited = [[0]*(n) for _ in range(n)] #적록색약용
for i in range(n):#적록색약용
    for j in range(n):
        if arr[i][j] == 'G':
            arr[i][j] = 'R'

for i in range(n):
    for j in range(n):
        if visited[i][j] == False:
            dfs(i,j)
            b+=1
print(a,b)