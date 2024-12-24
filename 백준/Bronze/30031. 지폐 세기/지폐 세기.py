a=int(input())
cnt=0
for _ in range(a):
    a,b = map(int, input().split())
    if b==68 and a==136:
        cnt+=1000
    elif b==68 and a==142:
        cnt+=5000
    elif b==68 and a==148:
        cnt+=10000
    elif b==68 and a==154:
        cnt+=50000
print(cnt)