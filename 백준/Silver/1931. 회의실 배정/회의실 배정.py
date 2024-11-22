import sys
n = int(sys.stdin.readline())
arr = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

start, end, result = 0,0,0
arr.sort(key=lambda x:(x[1], x[0]))
for newStart, newEnd in arr:
    if newStart>=end:
        result+=1
        end = newEnd
print(result)
