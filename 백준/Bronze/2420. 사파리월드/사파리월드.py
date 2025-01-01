a,b = map(int, input().split())
if a<b:
    print(abs(b-a))
elif a>b:
    print(abs(a-b))
else:
    print(0)