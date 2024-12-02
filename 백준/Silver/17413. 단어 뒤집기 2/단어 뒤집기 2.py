import sys
str = sys.stdin.readline().rstrip()
flag = False
string = ""
for i in range(len(str)):
    if i==0 and str[i]=="<" or str[i]=="<":
        flag = True
        print(str[i], end="")
    elif str[i]==">":
        print(str[i], end="")
        flag = False
    elif flag == True:
        print(str[i], end="")
    elif str[i]==" ":
        print(string[::-1], end=" ")
        string=""
    elif i!=len(str)-1 and str[i+1]=="<":
        string+=str[i]
        print(string[::-1], end="")
        string=""
    elif i+1 == len(str):
        string+=str[i]
        print(string[::-1])
    else:
        string+=str[i]