a=int(input())
b=int(input())
arr=[]
for i in range(a, b+1):
    flag = False
    for j in range(2,i//2+1):
        if i%j==0:
            flag = True
    if flag==False and i!=1:
        arr.append(i)
if len(arr)==0:
    print(-1)
else: 
    print(sum(arr))
    print(arr[0])