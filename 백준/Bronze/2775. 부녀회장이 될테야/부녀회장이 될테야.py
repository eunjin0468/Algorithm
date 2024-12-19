t = int(input())
for _ in range(t):
    k = int(input()) #동
    n = int(input()) #호수
    cnt = 0
    arr = [i for i in range(1, n+1)]
    for i in range(k):
        for j in range(1, n):
            arr[j]+=arr[j-1]
    print(arr[-1])