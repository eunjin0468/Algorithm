import sys
input = sys.stdin.readline

def dfs(v, i):
    visited[v] = 1
    w = arr[v]
    if not visited[w]:
        dfs(w, i)
    elif visited[w] and w==i:
        res.append(w)

n = int(input())
arr = [0]+[int(input()) for _ in range(n)]
res = []

for i in range(1, n+1):
    visited = [0]*(n+1)
    dfs(i,i)
    
print(len(res))
res.sort()
print('\n'.join(map(str, res)))