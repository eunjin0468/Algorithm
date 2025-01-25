while True:
    word = input()
    flag = False
    if word=='*':
        break
    d=1
    while d<len(word)-1:
        check = set()
        for i in range(len(word)-d):
            str = word[i]+word[i+d]
            if str in check:
                flag = True
                break
            else:
                check.add(str)
        d+=1
    print(word, end=' ')
    if flag == False:
        print('is surprising.')
    else:
        print('is NOT surprising.')