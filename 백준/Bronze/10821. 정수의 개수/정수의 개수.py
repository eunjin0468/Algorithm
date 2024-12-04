arr = list(map(int, input().split(',')))
num=0
for ans in arr:
    if type(ans)==int:
        num+=1
print(num)