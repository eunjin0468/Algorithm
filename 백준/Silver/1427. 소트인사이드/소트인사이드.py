str = input()
arr = []
for i in str:
    arr.append(i)
arr.sort(reverse=True)
for i in arr:
    print(i, end='')