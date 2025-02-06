import sys
sys.setrecursionlimit(10000)

a,b,c = map(int, input().split())
graph = [[0]*b for _ in range(a)]

def dfs(y, x, cnt):
    graph[y][x] = 1 #방문처리
    for dy, dx in arr:
        yy,xx = dy+y, dx+x
        if (0<=yy<a) and (0<=xx<b) and graph[yy][xx]==0:
            cnt = dfs(yy,xx,cnt+1)
    return cnt

for _ in range(c):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            graph[i][j] = 1
            
arr = [(-1,0), (1,0), (0,-1), (0,1)]
ans = []
for i in range(a):
    for j in range(b):
        if graph[i][j]==0: #빈 공간
            ans.append(dfs(i,j,1))

print(len(ans))
print(*sorted(ans))