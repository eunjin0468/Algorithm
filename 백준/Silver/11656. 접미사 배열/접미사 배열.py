str = input()
arr = [str]
for i in range(len(str)):
    n = str[i+1:]
    if n != '':
        arr.append(n)
arr.sort()
for string in arr:
    print(string)
