n,m = map(int, input().split())
arr = [i for i in range(1,n+1)]
for i in range(m):
    i,j = map(int, input().split())
    tmp = arr[i-1:j]
    tmp.reverse()
    arr[i-1:j] = tmp
print(' '.join(map(str,arr)))