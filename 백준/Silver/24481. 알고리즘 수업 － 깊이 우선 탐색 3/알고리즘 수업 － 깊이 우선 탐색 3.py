import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

n,m,r = map(int, input().split())
cnt = 0
graph=[[] for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b) #무방향 그래프
    graph[b].append(a)

def dfs(r):
    global cnt
    graph[r].sort()
    for n in graph[r]:
        if visited[n]==-1:
            visited[n]=visited[r]+1
            dfs(n)
visited[r]=0
dfs(r)
for i in visited[1:]:
    print(i)