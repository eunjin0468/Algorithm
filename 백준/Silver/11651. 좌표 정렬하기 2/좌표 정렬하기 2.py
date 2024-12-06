n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
arr.sort(key=lambda x:(x[1], x[0]))
for i in arr:
    print(i[0], i[1])