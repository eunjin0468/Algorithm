from collections import deque
import sys
n = int(input())
arr_A = list(map(int, input().split()))
arr_B = list(map(int, input().split()))
m = int(input())
arr_C = list(map(int, input().split()))
queue = deque([])

for i in range(n):
    if arr_A[i]==0:
        queue.appendleft(arr_B[i])
    '''else:
        if not queue:
            print(*arr_C)
            sys.exit()'''
for i in range(m):
    queue.append(arr_C[i])
    print(queue.popleft(), end=" ")