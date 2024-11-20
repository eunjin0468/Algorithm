n = int(input())
arr = list(map(int, input().split()))
arr.sort()
list=[]
cnt = 0
for i in range(len(arr)):
    if i==0:
        list.append(arr[i])
        cnt+=arr[i]
    else:
        cnt+=arr[i]
        list.append(cnt)
print(sum(list))