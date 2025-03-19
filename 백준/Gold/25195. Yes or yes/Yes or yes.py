import sys
input = sys.stdin.readline
sys.setrecursionlimit(100001)

n,m = map(int, input().split())
graph=[[] for _ in range(n+1)]
for _ in range(m):
    a,b = map(int, input().split())
    graph[a].append(b)
S = int(input())
s = list(map(int, input().split()))
flag = False
def dfs(i):
    global flag
    if i in s:
        return
    
    if graph[i]==[]:
        flag = True
        
    for j in graph[i]:
        if graph[j]!=[]:
            dfs(j)
        elif j not in s and graph[j]==[]:
            flag = True

dfs(1)
if flag == True:
    print("yes")
else:
    print("Yes")
