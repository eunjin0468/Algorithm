n = int(input())
arr = list(map(int, input().split()))
cnt = 0
for num in arr:
    if num == n:
        cnt+=1
print(cnt)