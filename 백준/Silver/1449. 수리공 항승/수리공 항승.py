n,l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
cnt = 1
start = arr[0]
for i in arr[1:]:
    if (i+0.5)-(start-0.5)<=l:
        continue
    else:
        cnt+=1
        start = i
print(cnt)