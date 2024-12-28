import heapq
t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    heapq.heapify(arr)
    ans = 0
    while len(arr)>1:
        tmp = 0
        a,b = heapq.heappop(arr), heapq.heappop(arr)
        tmp += a+b
        ans += tmp
        heapq.heappush(arr, tmp)
    print(ans)