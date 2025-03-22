from collections import deque
import sys
input = sys.stdin.readline

n,m = map(int, input().split())
ans = []
arr = [[] for _ in range(n+1)]
inDegree = [0 for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    inDegree[b]+=1

q = deque()
for i in range(1, n+1):
    if inDegree[i]==0:
        q.append(i)

while q:
    tmp = q.popleft()
    ans.append(tmp)
    for i in arr[tmp]:
        inDegree[i]-=1
        if inDegree[i]==0:
            q.append(i)

print(*ans)