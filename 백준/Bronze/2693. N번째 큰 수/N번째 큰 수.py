n = int(input())
for _ in range(n):
    arr = sorted(list(map(int, input().split())))
    print(arr[-3])