while True:
    str = input()
    if str == "0":
        break
    else:
        cnt = 0
        for i in range(len(str)):
            if str[i]==str[-i-1]:
                cnt+=1
        if cnt == len(str):
            print("yes")
        else:
            print("no")