n = int(input())
for i in range(1, n+1):
    a,b = input().split()
    a = int(a)-1
    b = b[:a] + b[a+1:]
    print(b)