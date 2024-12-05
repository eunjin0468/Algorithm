from itertools import combinations 
import sys
t = int(input())
for _ in range(t):
    dic = {}
    result = 1
    n = int(input())
    for _ in range(n):
        a,b = sys.stdin.readline().split()
        if b not in dic:
            dic[b] = 1
        else:
            dic[b]+=1
    for i in dic:
        result*=dic[i]+1 #상/하의 안 입는 경우
    print(result-1) #모든 옷을 안 입는 경우