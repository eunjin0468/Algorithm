n = int(input())
dasom = int(input())
arr = [int(input()) for _ in range(n-1)]
arr.sort(reverse=True)
cnt = 0
if n == 1:
    print("0")
else:
    while dasom <= arr[0]:
        dasom += 1
        arr[0] -= 1
        cnt += 1
        arr.sort(reverse=True)
    print(cnt)