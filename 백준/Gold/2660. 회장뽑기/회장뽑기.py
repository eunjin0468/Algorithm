from collections import deque
n = int(input())
graph = [[] for _ in range(n+1)]
score = 50
arr = []

def bfs(i):
    visited = [-1]*(n+1) #방문하지 않은 노드
    visited[i] = 0
    q = deque([i])
    while q:
        v = q.popleft()
        for w in graph[v]:
            if visited[w]==-1:
                visited[w]=visited[v]+1
                q.append(w)
    return max(visited)

while 1:
    a,b = map(int, input().split())
    if a==b==-1:
        break
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, n+1):
    tmp = bfs(i)
    if tmp < score: #회장은 회원들 중에서 점수가 가장 작은 사람
        score = tmp
        arr = [i] #회장 후보에 추가 (기존 후보들을 점수가 더 크므로 삭제)
    elif tmp == score: #회장 후보
        arr.append(i)
print(score, len(arr))
print(*arr)