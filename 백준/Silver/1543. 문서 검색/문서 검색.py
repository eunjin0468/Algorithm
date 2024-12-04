str = input().strip()
s = input().strip()
i,num = 0,0
while i<len(str):
    if s == str[i:i+len(s)]:
        num+=1
        i+=len(s)
    else:
        i+=1
print(num)