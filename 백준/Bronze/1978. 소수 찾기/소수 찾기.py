n = int(input())
arr = list(map(int, input().split()))
result=0
for i in range(len(arr)):
    cnt=0
    if arr[i]==1:
        continue
    for j in range(2,arr[i]):
        if arr[i]%j ==0:
            cnt+=1
    if cnt==0:
        result+=1
print(result)