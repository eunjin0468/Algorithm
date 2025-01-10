import math
n = int(input())
tree = int(input())
arr = [] #나무 사이 간격
for i in range(n-1):
    a = int(input())
    arr.append(a-tree)
    tree = a

#arr에 들어있는 최대공약수 찾기
g = arr[0]
for i in range(1, len(arr)): 
    g = math.gcd(g, arr[i])

#둘 사이 심을 가로수 갯수 : 간격//최대공약수-1
result = 0
for each in arr:
    result += each//g-1
print(result)