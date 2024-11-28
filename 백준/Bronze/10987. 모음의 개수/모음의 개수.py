input = input()
str = "aeiou"
cnt=0
for i in range(len(input)):
    if input[i] in str:
        cnt+=1
print(cnt)