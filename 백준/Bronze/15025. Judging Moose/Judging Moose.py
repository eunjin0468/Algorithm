a,b = map(int, input().split())
if a==0 and b==0:
    print("Not a moose")
elif a!=b:
    print(f"Odd {max(a,b)*2}")
elif a==b:
    print(f"Even {b*2}")
