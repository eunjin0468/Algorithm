import sys, heapq
input = sys.stdin.readline
n,k = map(int, input().split())
jewerly = [list(map(int, input().split())) for _ in range(n)]
bags = [int(input()) for _ in range(k)]
jewerly.sort() 
bags.sort()
tmp = []
res = 0

for bag in bags:
    while jewerly and bag>=jewerly[0][0]:
        heapq.heappush(tmp, -jewerly[0][1])
        heapq.heappop(jewerly)
    if tmp:
        res+=heapq.heappop(tmp)
    elif not jewerly:
        break
        
print(-res)