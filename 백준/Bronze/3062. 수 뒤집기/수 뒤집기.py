t = int(input())
for _ in range(t):
    a = input()
    b = a[::-1]
    c = str(int(a)+int(b)) 
    d = c[::-1]
    if c==d:
        print("YES")
    else:
        print("NO")