n = int(input())
arr = [int(input()) for _ in range(n)]
plus, minus = [],[]
result = 0 
for num in arr:
    if num==1:
        result+=1
    elif num>0:
        plus.append(num)
    else:
        minus.append(num)
plus.sort()
minus.sort(reverse=True)
while len(plus)!=0:
    if len(plus)==1:
        result+=plus.pop()
    else:
        result+=plus.pop()*plus.pop()
while len(minus)!=0:
    if len(minus)==1:
        result+=minus.pop()
    else:
        result+=minus.pop()*minus.pop()
print(result)