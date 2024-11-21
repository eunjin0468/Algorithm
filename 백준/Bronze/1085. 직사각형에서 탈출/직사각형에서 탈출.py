x,y,w,h = map(int, input().split())

arr = []
arr.append(abs(x-w))
arr.append(abs(y-h))
arr.append(x-0)
arr.append(y-0)
print(min(arr))