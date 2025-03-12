from collections import deque

n = int(input())
m = int(input())
arr = [[] for _ in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

def bfs(start):
    q = deque()
    q.append(start)
    visited[start] = 1
    cnt = 0
    depth = 0

    while q:
        depth += 1
        for _ in range(len(q)):
            friend = q.popleft()
            for f in arr[friend]:
                if not visited[f]:
                    visited[f] = 1
                    q.append(f)
                    cnt+=1
        if depth == 2:
            return(cnt)

r = bfs(1)
if r == None:
    print(0)
else:
    print(r)