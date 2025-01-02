a = list(input())
b = list(input())
tmp = []
ans = ''

for i in range(8):
    ans += a[i]+b[i]

while len(ans)!=2:
    for i in range(len(ans)-1):
        tmp.append(str((int(ans[i])+int(ans[i+1]))%10))
    ans = ''.join(tmp)
    tmp = []
print(ans)