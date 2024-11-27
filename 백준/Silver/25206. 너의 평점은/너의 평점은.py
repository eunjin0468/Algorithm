arr = [input().split() for _ in range(20)]
sum, cl =0,0
for a,b,c in arr:
    b = float(b)
    cl+=int(b)
    if c == "A+":
        sum += b*4.5
    elif c == "A0":
        sum += b*4.0
    elif c == "B+":
        sum += b*3.5
    elif c == "B0":
        sum += b*3.0
    elif c == "C+":
        sum += b*2.5
    elif c == "C0":
        sum += b*2.0
    elif c == "D+":
        sum += b*1.5
    elif c == "D0":
        sum += b*1.0
    elif c == "F":
        sum += 0
    elif c == "P":
        cl-=int(b)
print(round(sum/cl, 6))