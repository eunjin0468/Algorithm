from collections import deque
import sys
input = sys.stdin.readline

#입력
n,m,r = map(int, input().split())
graph = [[] for _ in range(n+1)]
visited=[0]*(n+1)
visited[r]=1
cnt=1
q=deque([r])

#양방향 간선 생성
for _ in range(m): 
    a,b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#내림차순 정렬
for i in range(1, n+1):
    graph[i].sort(reverse=True)

while q:
    v = q.popleft()
    for i in graph[v]:
        if visited[i]:
            continue 
        cnt+=1
        visited[i]=cnt
        q.append(i)
print(*visited[1:], sep='\n')