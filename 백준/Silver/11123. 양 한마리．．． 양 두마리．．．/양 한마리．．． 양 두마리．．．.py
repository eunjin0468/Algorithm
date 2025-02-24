import sys
sys.setrecursionlimit(100000)

t = int(input())
dx = [0,0,-1,1]
dy = [-1,1,0,0]
def dfs(i,j):
    global cnt
    arr[i][j] = '.'
    for n in range(4):
        x,y = dx[n]+i, dy[n]+j
        if 0<=x<a and 0<=y<b and arr[x][y] == '#':
            dfs(x,y)

for _ in range(t):
    a,b = map(int, input().split())
    arr = [list(input()) for _ in range(a)]
    cnt = 0
    for i in range(a):
        for j in range(b):
            if arr[i][j] == '#':
                dfs(i,j)
                cnt+=1
    print(cnt)