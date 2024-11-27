arr = [list(map(int, input().split())) for _ in range(4)]
sum = 0
list = []
for i in range(4):
    sum-=arr[i][0]
    sum+=arr[i][1]
    list.append(sum)
print(max(list))
