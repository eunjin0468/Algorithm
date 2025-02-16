n = int(input()) #전체 사람의 수
a,b = map(int, input().split()) #촌수1 촌수2
m = int(input()) #부모자식 수
graph = [[] for _ in range(n+1)]
visited = [0]*(n+1)
result = []
for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)
def dfs(a,cnt):
    cnt+=1
    visited[a]=1
    if a==b:
        result.append(cnt)
    for i in graph[a]:
        if not visited[i]:
            dfs(i,cnt)
dfs(a,0)
if len(result)==0:
    print(-1)
else:
    print(result[0]-1)