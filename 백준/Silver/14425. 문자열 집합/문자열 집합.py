import sys
a,b = map(int, sys.stdin.readline().split())
str = dict()
cnt = 0
for _ in range(a):
    s = sys.stdin.readline().rstrip()
    str[s] = True
for _ in range(b):
    d = sys.stdin.readline().rstrip()
    if d in str:
        cnt+=1
print(cnt)