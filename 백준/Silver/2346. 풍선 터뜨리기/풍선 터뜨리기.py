from collections import deque
n = int(input())
q = deque(enumerate(map(int, input().split())))
res = []
while q:
    idx, ballon = q.popleft()
    res.append(idx+1)
    if ballon>0:
        q.rotate(-(ballon-1))
    else:
        q.rotate(-ballon)
print(' '.join(map(str, res)))