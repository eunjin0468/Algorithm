a = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b,c = map(int, input().split())
ans = ""
while b!=0:
    ans=a[b%c]+ans
    b//=c
print(ans)