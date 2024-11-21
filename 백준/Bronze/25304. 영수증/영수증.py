sum = int(input())
num = int(input())
cnt = 0
for i in range(num):
    a,b = map(int, input().split())
    cnt+=a*b
if cnt == sum:
    print("Yes")
else:
    print("No")