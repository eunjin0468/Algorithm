n,m = map(int, input().split())
res = []
def dfs(start):
    if len(res)==m:
        print(*res)
    else:
        for i in range(start, n+1):
            res.append(i)
            dfs(i)
            res.pop()
dfs(1)