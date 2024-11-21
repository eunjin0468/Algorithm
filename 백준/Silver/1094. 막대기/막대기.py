n = int(input())
arr = [64,32,16,8,4,2,1]
cnt = 0
count =0
while cnt<n:
    for i in range(len(arr)):
        if cnt+arr[i]<=n:
            cnt+=arr[i]
            count+=1
        if cnt==n:
            break
print(count)