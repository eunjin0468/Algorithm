import sys
input=sys.stdin.readline
sys.setrecursionlimit(10**9)

n,m = map(int, input().split())
arr = [[] for _ in range(n+1)]

def dfs(start, end, chk):
    global cnt
    if start == end:
        cnt = chk
        return
    for i,j in arr[start]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, end, chk+j)

for _ in range(n-1):
    c,d,e = map(int, input().split())
    arr[c].append([d,e])
    arr[d].append([c,e])
for _ in range(m):
    start,end = map(int, input().split())
    visited = [0]*(n+1)
    cnt = 0
    visited[start] = 1
    dfs(start, end, 0)
    print(cnt)