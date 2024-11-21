n = int(input())
arr = []
for _ in range(n):
    a,b = input().split()
    arr.append((int(a), b))
for i in sorted(arr, key=lambda x:x[0]):
    print(i[0], i[1])