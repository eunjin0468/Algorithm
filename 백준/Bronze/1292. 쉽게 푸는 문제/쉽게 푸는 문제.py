a,b = map(int, input().split())
sum, arr = 0, []
for i in range(1, b+1):
    for j in range(i):
        arr.append(i)
for i in range(a, b+1):
    sum+=arr[i-1]
print(sum)