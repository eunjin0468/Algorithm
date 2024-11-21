n = int(input())
arr = list(map(int, input().split()))
num= int(input())
cnt = 0 
for i in range(len(arr)):
    if arr[i] == num:
        cnt+=1
print(cnt)