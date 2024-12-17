h,m = map(int, input().split())
num = int(input())
h += num//60
m += num%60
if m>=60:
    h+=1
    m-=60
if h>=24:
    h-=24
print(h,m)