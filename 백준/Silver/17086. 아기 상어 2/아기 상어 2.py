import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
d = [(-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1)]

def bfs(y, x):
    visited = [[0] * m for _ in range(n)] 
    q = deque()
    q.append((y, x))
    visited[y][x] = 1  

    while q:
        y, x = q.popleft()
        for dy, dx in d:
            Y, X = y + dy, x + dx
            if 0 <= X < m and 0 <= Y < n and visited[Y][X] == 0:
                if arr[Y][X] == 0:  # 빈 공간이면 계속 탐색
                    q.append((Y, X))
                    visited[Y][X] = visited[y][x] + 1
                else:  # 상어를 만나면 거리 반환
                    return visited[y][x]

    return 0  # 상어가 없는 경우

ans = 0
for y in range(n):
    for x in range(m):
        if arr[y][x] != 1:  # 상어가 없는 곳만 BFS 실행
            temp = bfs(y, x)  
            ans = max(ans, temp) 

print(ans)