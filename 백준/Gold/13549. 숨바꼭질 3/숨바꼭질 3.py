import sys
from collections import deque

input = sys.stdin.readline

a, b = map(int, input().split())
MAX = 10**5
visited = [-1] * (MAX + 1)  # 방문하지 않은 노드는 -1로 설정

def bfs(a, b):
    q = deque([a])
    visited[a] = 0  # 시작점은 0초

    while q:
        x = q.popleft()

        if x == b:
            return visited[x]  # 정답 반환

        for nx in (2*x, x-1, x+1):
            if 0 <= nx <= MAX and visited[nx] == -1:  # 방문하지 않은 경우만 탐색
                if nx == 2*x:  # 순간이동: 시간이 증가하지 않음
                    visited[nx] = visited[x]
                    q.appendleft(nx)  # 우선 탐색
                else:  # 걷기(이동)
                    visited[nx] = visited[x] + 1
                    q.append(nx)

print(bfs(a, b))
