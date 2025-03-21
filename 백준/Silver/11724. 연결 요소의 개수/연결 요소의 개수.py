import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]
visited = [1]+[0]*(n)
cnt=0

for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def dfs(node):
    visited[node]=1
    for k in arr[node]:
        if visited[k]==0:
            dfs(k)

for v in range(len(visited)):
    if v!=0 and visited[v]==0:
        cnt+=1
        dfs(v)
    else:
        continue
    
print(cnt)