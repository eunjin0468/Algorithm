import heapq
import sys

n = int(sys.stdin.readline())
left, right, answer = [], [], []

for _ in range(n):
    num = int(sys.stdin.readline())
    
    if len(left) == len(right):
        heapq.heappush(left, (-num, num))  # 최대 힙
    else:
        heapq.heappush(right, (num, num))  # 최소 힙
    
    # 힙 간 값의 불균형이 있으면 교환
    if right and left[0][1] > right[0][0]:
        min_val = heapq.heappop(right)[0]  # right에서 최소값 추출
        max_val = heapq.heappop(left)[1]  # left에서 최대값 추출
        heapq.heappush(left, (-min_val, min_val))  # left에 min_val 추가
        heapq.heappush(right, (max_val, max_val))  # right에 max_val 추가
    
    # 현재 중앙값 추가
    answer.append(left[0][1])

for ans in answer:
    print(ans)
