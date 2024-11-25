str = input()
cnt=0
    
for i in range(len(str)):
    if str[i]==str[-i-1]:
        #print(str[i], str[-i-1])
        cnt+=1
if len(str)==cnt:
    print(1)    
else:
    print(0)