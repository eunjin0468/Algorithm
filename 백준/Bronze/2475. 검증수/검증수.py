arr = list(map(int, input().split()))
sum = 0
for num in arr:
    sum+=num**2
print(sum%10)