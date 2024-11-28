str = input()
univ = "CAMBRIDGE"
for i in range(len(univ)):
    if univ[i] in str:
        str = str.replace(univ[i], "")
print(str)