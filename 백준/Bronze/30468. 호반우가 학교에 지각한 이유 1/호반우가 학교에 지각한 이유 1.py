a,b,c,d,e = map(int, input().split())
if (a+b+c+d)/4>=e:
    print(0)
else:
    print(e*4-(a+b+c+d))