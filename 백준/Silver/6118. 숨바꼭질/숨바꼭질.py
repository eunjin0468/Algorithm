from collections import deque
n,m = map(int, input().split()) #헛간노드, 길엣지
graph = [[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
chk = [0]*(n+1)
def bfs(s):
    q = deque()
    q.append(s)
    chk[s] = 1
    while q:
        s = q.popleft()
        for i in graph[s]:
            if not chk[i]:
                chk[i] = chk[s]+1 #각 노드의 거리 기록
                q.append(i)
bfs(1)
print(chk.index(max(chk)), max(chk)-1, chk.count(max(chk)))