a = int(input())
b = str(a)
if a%7!=0 and '7' not in b:
    print(0)
elif a%7==0 and '7' not in b:
    print(1)
elif a%7!=0 and '7' in b:
    print(2)
else:
    print(3)