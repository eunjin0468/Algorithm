n = int(input())
str = input()
l_num = str.count("LL")
if l_num<=1:
    print(len(str))
else:
    print((len(str)-l_num)+1)