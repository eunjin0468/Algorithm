from collections import deque
a,k = map(int, input().split())
q = deque([a])
visited = {a:0}
while q:
    c = q.popleft()
    if c==k:
        break
    for x in [2*c, 1+c]:
        if x>k or x in visited:
            continue
        visited[x] = visited[c]+1 #연산 횟수 카운트
        q+=[x]
print(visited[k])