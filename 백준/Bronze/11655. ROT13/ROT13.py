str = list(input())
arr = []
for i in range(len(str)):
    s = ord(str[i])
    if s!=32: 
        if s>64 and s<91 or s>96 and s<123: #영문자일때만    
            if s>=78 and s<91:
                s = s+13-26
            elif s>=110 and s<123:
                s = s+13-26
            else:
                s+=13
        arr.append(chr(s))
    else: 
        arr.append(" ")
for ans in arr:
    print(ans, end='')