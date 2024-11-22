import heapq
import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
arr.sort(key=lambda x:x[0])
room=[]
heapq.heappush(room, arr[0][1]) 

for i in range(1, n):
    if arr[i][0] < room[0]:
        heapq.heappush(room, arr[i][1])
    else:
        heapq.heappop(room)
        heapq.heappush(room, arr[i][1])
print(len(room))