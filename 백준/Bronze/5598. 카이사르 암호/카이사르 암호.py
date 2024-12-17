arr = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
str = list(input())
s = ''
for i in range(len(str)):
    index = arr.index(str[i])
    if index<3:
        index+=23
        s+=arr[index]
    else:
        index-=3
        s+=arr[index]
print(''.join(s))