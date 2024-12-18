a = int(input())
b = list(map(int, input().split()))
c=0
max = b[0]

for i in range(a):
    if b[i] > max:
        max = b[i]

for i in range(a):
     c += b[i]/max*100

avg = c/a
print(avg)
