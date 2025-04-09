import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    parent = [0]*(n+1)
    for _ in range(n-1):
        a,b = map(int, input().split())
        parent[b]=a

    ta,tb = map(int, input().split())
    tracking_ta = [] #a 부모 경로
    
    # 1.ta의 조상 리스트 생성
    while True:
        if ta==0:
            break
        tracking_ta.append(ta)
        ta = parent[ta]

	# 2.tb의 조상을 따라가며 공통 조상 찾기
    while True:
        if tb in tracking_ta:
            print(tb)
            break
        tb = parent[tb]
