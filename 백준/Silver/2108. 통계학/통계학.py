import statistics
import sys
n = int(sys.stdin.readline())
arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
print(round(sum(arr)/n))
print(arr[n//2])

dic = dict()
for i in arr:
    if i in dic:
        dic[i] += 1
    else:
        dic[i] = 1
mx = max(dic.values()) 
result = []
for i in dic:
    if mx == dic[i]:
        result.append(i)
if len(result) > 1:
    print(result[1])
else:
    print(result[0])
print(arr[-1]-arr[0])