import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(p):
    global cnt
    visited[p] = True
    ans[p] = cnt
    graph[p].sort(reverse=True) 
    for i in graph[p]:
        if not visited[i]:
            cnt+=1
            dfs(i)
    
n,m,p = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited = [False]*(n+1)
ans = [0]*(n+1)
cnt = 1
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
dfs(p)
for i in ans[1:]:
    print(i)