t = int(input())

def num(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return num(n-1)+num(n-2)+num(n-3)

for _ in range(t):
    n = int(input())
    print(num(n))