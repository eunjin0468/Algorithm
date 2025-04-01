import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
a,b = map(int, input().split())
graph = [[] for _ in range(a+1)]
visited = [0]*(a+1)
for _ in range(b):
    c,d = map(int, input().split())
    graph[d].append(c)
n = int(input())
cnt = 0
def dfs(n):
    global cnt
    visited[n] = 1
    for i in graph[n]:
        if not visited[i]:
            cnt+=1
            dfs(i)
dfs(n)
print(cnt)