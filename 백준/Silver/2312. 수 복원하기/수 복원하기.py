t = int(input())
for _ in range(t):
    n = int(input())
    arr = []
    for i in range(2, n+1):
        cnt = 0
        while n%i==0:
            cnt+=1
            n/=i
        if cnt:
            arr.append([i, cnt])
    for a in arr:
        print(*a)