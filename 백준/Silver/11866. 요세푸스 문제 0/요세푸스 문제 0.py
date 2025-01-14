from collections import deque
import sys

a,b = map(int, input().split())
q = deque([i for i in range(1, a+1)]) #양방향 연결리스트 생성

res = []
while len(q)!=0:
    for _ in range(b-1):
        q.append(q.popleft()) #q의 맨 앞의 두 요소 삭제후 뒤에 이어붙임
    res.append(str(q.popleft())) #b번째 요소를 res에 추가
print("<"+", ".join(res)+">")