import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n,m,r = map(int, input().split())
cnt = 0
graph=[[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b) #무방향 그래프
    graph[b].append(a)  

for i in range(1, n+1):
    graph[i].sort(reverse=True)

depth = [-1]*(n+1)  #깊이 저장
visited_order = [0]*(n+1) #방문순서 저장

def dfs(r,d):
    global cnt
    cnt+=1
    depth[r] = d #깊이 저장
    visited_order[r] = cnt #방문순서 저장
    
    for n in graph[r]:
        if depth[n]==-1:
            dfs(n,d+1)

dfs(r,0)

ans=0
for i in range(1,n+1):
    if depth[i]!=-1:
        ans+=(depth[i]*visited_order[i])
print(ans)