while True:
    a,b,c = map(int, input().split())
    m = max(a,b,c)
    n = a+b+c-m
    if a==b==c==0:
        break
    else:
        if m >= n:
            print("Invalid")
        elif a==b==c:
            print("Equilateral")
        elif a==b or b==c or a==c:
            print("Isosceles")
        else:
            print("Scalene")