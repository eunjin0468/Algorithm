import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
m = int(input())
arr = []
parent = [num for num in range(n+1)]

for _ in range(m):
    a,b,cost = map(int, input().split())
    arr.append((cost,a,b))
arr.sort()
ans = 0

#노드가 속한 대표루트노드를 찾는 함수
def find(parent,x): 
    if parent[x]!=x:
        parent[x] = find(parent, parent[x])
    return parent[x]

#두 개의 노드를 같은 집합으로 합치는 함수
def union(parent,a,b):
    a = find(parent, a)
    b = find(parent, b)
    if a>b:
        parent[b] = a
    else:
        parent[a] = b

for edge in arr:
    cost, a, b = edge
    if find(parent,a) != find(parent,b): 
        union(parent,a,b)
        ans+=cost

print(ans)