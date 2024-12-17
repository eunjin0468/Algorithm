n = int(input())
for _ in range(n):
    str = input().rstrip()
    arr = []
    s=''
    for i in range(len(str)):
        if str[i]!=' ' or str[i]!='\n':
            s+=str[i].strip()
        if str[i]==' ':
            arr.append(s[::-1])
            arr.append(' ')
            s=''
        if i==len(str)-1:
            arr.append(s[::-1])
    print(''.join(arr))