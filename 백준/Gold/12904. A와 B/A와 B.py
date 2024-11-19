str1 = input()
str2 = input()

while len(str1)!=len(str2):
    if str2[-1] == "A":
        str2 = str2[:-1]
    elif str2[-1] == "B":
        str2 = str2[:-1]
        str2 = str2[::-1]
if str1 == str2:
    print(1)
else:
    print(0)
