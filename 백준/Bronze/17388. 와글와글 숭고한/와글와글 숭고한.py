a,b,c = map(int, input().split())
if a+b+c >= 100:
    print("OK")
else:
    arr = [a,b,c]
    if min(arr) == a:
        print("Soongsil")
    elif min(arr) == b:
        print("Korea")
    elif min(arr) == c:
        print("Hanyang")