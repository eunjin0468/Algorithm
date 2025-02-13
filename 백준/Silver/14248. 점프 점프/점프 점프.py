import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n = int(input())
arr = list(map(int, input().split()))
start = int(input())
visited = [0]*n
cnt=1
def dfs(x):
    global cnt
    for nx in (x+arr[x],x-arr[x]):
       if 0<=nx<n and visited[nx]==0:
           cnt+=1
           visited[nx]=1
           dfs(nx)
dfs(start-1)
print(cnt)