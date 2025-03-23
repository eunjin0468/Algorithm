import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

n,m,r = map(int, input().split())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    a,b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

for i in range(1, n+1):
    arr[i].sort()  

def dfs(node, d):
    global cnt
    cnt+=1 #방문순서 증가
    depth[node] = d
    visited_order[node] = cnt
    for i in arr[node]:
        if depth[i]==-1:
            dfs(i, d+1)

depth = [-1]*(n+1)  #깊이 저장
visited_order = [0]*(n+1) #방문순서 저장
cnt, res = 0, 0
dfs(r,0)

for i in range(1, n+1):
    if depth[i]!=-1:
        res += (depth[i]*visited_order[i])

print(res)