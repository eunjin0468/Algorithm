a,b = map(int, input().split())
cnt = 0
arr = []
for i in range(1, a+1):
    if a%i==0:
        cnt+=1
        arr.append(i)
    if cnt==b:
        print(i)
        break
if len(arr)<b:
    print(0)