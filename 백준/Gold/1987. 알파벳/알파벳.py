n,m = map(int, input().split())
arr = [list(input()) for _ in range(n)]
res = set()
d = [[-1,0],[1,0],[0,1],[0,-1]]
ans = 0
def dfs(x,y,cnt):
    global ans
    ans = max(ans, cnt)
    for k in range(4):
        nx, ny = x+d[k][0], y+d[k][1]
        if 0<=nx<n and 0<=ny<m and arr[nx][ny] not in res:
            res.add(arr[nx][ny])
            dfs(nx, ny, cnt+1)
            res.remove(arr[nx][ny])
res.add(arr[0][0])
dfs(0,0,1)
print(ans)