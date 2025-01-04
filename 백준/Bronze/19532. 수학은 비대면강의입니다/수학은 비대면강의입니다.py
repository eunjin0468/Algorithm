import sys
a,b,c,d,e,f = map(int, sys.stdin.readline().split())
x = ((e*c)-(b*f)) // ((a*e)-(d*b))
y = ((a*f)-(d*c)) // ((a*e)-(d*b))
print(x, y)