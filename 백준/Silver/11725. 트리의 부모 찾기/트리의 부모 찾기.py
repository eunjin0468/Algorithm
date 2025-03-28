import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
arr = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

q = deque()
q.append(1)
ans = [0]*(n+1)

def bfs():
    while q:
        node = q.popleft()
        for next in arr[node]:
            if ans[next] == 0:
                ans[next] = node
                q.append(next)

bfs()
for x in ans[2:]:
    print(x)