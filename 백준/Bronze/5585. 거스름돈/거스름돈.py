n = 1000-int(input())
arr = [500,100,50,10,5,1]
cnt = 0
for coin in arr:
    cnt+=n//coin
    n%=coin
print(cnt)