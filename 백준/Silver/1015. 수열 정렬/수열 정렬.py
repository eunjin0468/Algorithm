n = int(input())
arr = list(map(int, input().split()))
l = []
arr_s = sorted(arr)
for i in arr:
    l.append(arr_s.index(i))
    arr_s[arr_s.index(i)]=-1
print(*l)