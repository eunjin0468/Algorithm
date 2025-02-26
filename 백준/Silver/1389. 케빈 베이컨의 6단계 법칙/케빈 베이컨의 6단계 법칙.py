from collections import deque
n,m = map(int, input().split()) #유저, 친구관계
graph = [[] for _ in range(n+1)]
res = []
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
def bfs(graph, i):
    visited = [0]*(n+1)
    num = [0]*(n+1)
    q = deque()
    q.append(i)
    visited[i]=1

    while q:
        j = q.popleft()
        for k in graph[j]:
            if visited[k]==0:
                visited[k]=1
                num[k]=num[j]+1
                q.append(k)
    return sum(num)
              
for i in range(1, n+1):
    res.append(bfs(graph, i))
print(res.index(min(res))+1)