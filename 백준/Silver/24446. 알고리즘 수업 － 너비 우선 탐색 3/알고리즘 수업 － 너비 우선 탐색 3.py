from collections import deque
import sys
input = sys.stdin.readline
n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [-1]*(n+1)
def bfs(node):
    q = deque([node])
    visited[node]=0
    while q:
        v = q.popleft()
        for g in graph[v]:
            if visited[g] == -1:
                visited[g] = visited[v]+1
                q.append(g)
        
bfs(r)
for i in visited[1:]:
    print(i)