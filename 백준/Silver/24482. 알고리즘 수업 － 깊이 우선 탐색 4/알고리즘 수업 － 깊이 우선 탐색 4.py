import sys
sys.setrecursionlimit(10 ** 8)
input = sys.stdin.readline

n,m,r = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(node):
    arr[node].sort(reverse=True)
    for n in arr[node]:
        if visited[n]==-1:
            visited[n] = visited[node]+1
            dfs(n)

visited[r] = 0
dfs(r)

for i in visited[1:]:
    print(i)