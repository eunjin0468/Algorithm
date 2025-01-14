from collections import deque
import sys
input = sys.stdin.readline
deq = deque()
a = int(input())

for _ in range(a):
    n = input().rstrip().split()
    if n[0] == '1':
        deq.appendleft(n[1])
    elif n[0]=='2':
        deq.append(n[1])
    elif n[0]=='3':
        if deq:
            print(deq.popleft())
        else:
            print(-1)
    elif n[0]=='4':
        if deq:
            print(deq.pop())
        else:
            print(-1)
    elif n[0]=='5':
        print(len(deq))
    elif n[0]=='6':
        if len(deq)==0:
            print(1)
        else:
            print(0)
    elif n[0]=='7':
        if deq:
            print(deq[0])
        else:
            print(-1)
    elif n[0]=='8':
        if deq:
            print(deq[-1])
        else:
            print(-1)