import sys
t = int(sys.stdin.readline())
arr=[]
for _ in range(t):
    arr.append(int(sys.stdin.readline()))
arr.sort()
print('\n'.join(map(str, arr)))