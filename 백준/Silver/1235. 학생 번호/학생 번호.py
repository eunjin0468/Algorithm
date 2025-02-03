n = int(input())
arr = [input() for i in range(n)]
cnt=0
for i in range(1, len(arr[0])+1):
    res = []
    for j in range(n):
        if arr[j][-i:] in res:
            break
        else:
            res.append(arr[j][-i:])
    if len(res)==n:
        print(i)
        break