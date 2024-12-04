t = int(input())
for i in range(t):
    n = int(input())
    arr = []
    for j in range(n):
        a, b = input().split()
        a = int(a)
        arr.append((a,b))
    arr.sort(reverse=True)
    print(arr[0][1])