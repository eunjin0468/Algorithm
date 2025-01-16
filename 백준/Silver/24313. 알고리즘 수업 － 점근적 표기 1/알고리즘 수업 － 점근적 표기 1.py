a0, a1 = map(int, input().split())
c = int(input())
n = int(input())

if (a0*n+a1) <= (c*n) and a0<=c:
    print(1)
else:
    print(0)