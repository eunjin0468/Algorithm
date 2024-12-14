n = int(input())
l = []
for i in range(n):
    sum_isdigit = 0
    arr = list(input())
    for str in arr:
        if str.isdigit():
            sum_isdigit+=int(str)
    l.append((''.join(arr),len(arr), sum_isdigit))
l.sort(key=lambda x:(x[1], x[2], x[0]))
for str in l:
    print(str[0])