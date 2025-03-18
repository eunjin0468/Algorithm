24444
import sys
from collections import deque
input = sys.stdin.readline

def bfs(r):
    q= deque([r])
    cnt = 1
    visited[r] = cnt
    while q:
        v = q.popleft()
        for node in arr[v]:
            if visited[node]==0:
                q.append(node)
                cnt+=1
                visited[node] = cnt

n,m,r = map(int, input().split())
visited = [0]*(n+1)
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    
for row in arr: #작은 숫자부터 방문
    row.sort()
bfs(r)
print(*visited[1:], sep='\n')