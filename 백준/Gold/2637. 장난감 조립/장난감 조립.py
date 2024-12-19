from collections import deque
n = int(input())
m = int(input())

next = [[] for _ in range(n+1)]
pre = [0]*(n+1) #x의 갯수
answer = [0]*(n+1)
answer[n] = 1 #최종본 

for _ in range(m):
    x,y,k = map(int, input().split())
    next[x].append((y,k))
    pre[y] += 1

queue = deque([n]) #처음에는 완성품 n만 포함
origin = [i for i in range(1, n+1) if not next[i]] #기본 부품 목록

while queue:
    tmp = queue.popleft()
    for a,b in next[tmp]:
        pre[a] -= 1
        answer[a] += b*answer[tmp]
        if not pre[a]:
            queue.append(a)
for i in origin:
    if i==0:
        pass
    else:
        print(i, answer[i])