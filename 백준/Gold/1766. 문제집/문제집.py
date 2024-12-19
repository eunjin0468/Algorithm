import heapq
n,m = map(int, input().split())
answer, queue = [], []
nexts = [[] for _ in range(n+1)] #이후에 풀 문제들
pre = [0 for _ in range(n+1)] #이전에 풀어야 할 문제의 개수

#먼저 풀어야 할 문제 업데이트
for i in range(m):
    a,b = map(int, input().split())
    nexts[a].append(b)
    pre[b] += 1

for i in range(n+1):
    if pre[i] == 0:
        heapq.heappush(queue, i)

while queue:
    tmp = heapq.heappop(queue)
    answer.append(tmp)
    for i in nexts[tmp]:
        pre[i]-=1
        if pre[i] == 0:
            heapq.heappush(queue, i)
print(' '.join(map(str, answer[1:])))