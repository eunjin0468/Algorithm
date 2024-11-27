n = int(input())
arr = [input() for _ in range(n)]
a = arr.count('1')
b = arr.count('0')
if a>b:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")