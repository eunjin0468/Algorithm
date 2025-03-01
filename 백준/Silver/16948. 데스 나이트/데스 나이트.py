from collections import deque
import sys
input = sys.stdin.readline
 
#입력
n = int(input())
d = [[-2,-1],[-2,1],[0,-2],[0,2],[2,-1],[2,1]]
r1,c1,r2,c2 = map(int, input().split())
graph = [[0]*n for _ in range(n)]
 
def bfs(y,x):
    queue = deque([(y,x)])
    graph[y][x]=1 #방문체크
 
    while queue:
        y,x = queue.popleft()
 
        if y==r2 and x==c2:
            return graph[y][x]-1
        for dy, dx in d:
            Y,X = y+dy, x+dx
            if 0<=Y<n and 0<=X<n and graph[Y][X]==0:
                queue.append([Y,X])
                graph[Y][X]=graph[y][x]+1
    return -1 #못 잡을 시 종료
 
print(bfs(r1,c1))