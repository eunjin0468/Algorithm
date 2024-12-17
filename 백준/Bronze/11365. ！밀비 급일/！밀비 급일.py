while True:
    str = list(input().split(" "))
    arr = []
    if str[0] == "END":
        break
    else:
        for i in range(len(str)):
            arr.append(str[i][::-1])
    arr = arr[::-1]
    print(' '.join(arr))