n = int(input())
arr=[]
for i in range(n):
    arr.append(int(input()))
arr.sort(reverse=True)
cnt = 0
for i in range(2, len(arr), 3):
    cnt+=arr[i]
print(sum(arr)-cnt)