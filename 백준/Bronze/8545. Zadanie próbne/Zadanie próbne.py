str = input()
list = []
for i in range(len(str)-1, -1, -1):
    list.append(str[i])
print(''.join(list))