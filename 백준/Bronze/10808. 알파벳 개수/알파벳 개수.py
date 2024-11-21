arr = [0]*26
str = input()
for i in (str):
    arr[ord(i)-97] = str.count(i)
for i in arr:
    print(i, end=" ")