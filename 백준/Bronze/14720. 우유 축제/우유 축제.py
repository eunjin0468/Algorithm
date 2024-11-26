n = int(input())
arr = list(map(int, input().split()))
result, cnt=0,0
for i in range(len(arr)):
    if arr[i]==0 and cnt==0 or arr[i]%3==0 and cnt==0:
        cnt+=1
        result+=1
    elif arr[i]%3==1 and cnt==1:
        cnt+=1
        result+=1
    elif arr[i]%3==2 and cnt==2:
        result+=1
        cnt=0
print(result)