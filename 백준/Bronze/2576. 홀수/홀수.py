cnt = 0
arr = []
while cnt<7:
    cnt+=1
    num = int(input())
    if num%2!=0:
        arr.append(num)
if len(arr) ==0:
    print("-1")
else:
    print(sum(arr))
    print(min(arr))