str = input()
result = set()
for i in range(len(str)):
    for j in range(i, len(str)):
        result.add(str[i:j+1])
print(len(result))