n = int(input())
result = 0
arr = list(map(int, input().split()))+[0]*(5-n)
if arr[0]>arr[2]:
    result += (arr[0]-arr[2])*508
else:
    result += (arr[2]-arr[0])*108
if arr[1]>arr[3]:
    result+=(arr[1]-arr[3])*212
else:
    result+=(arr[3]-arr[1])*305
if n==5:
    result+=arr[4]*707
print(result*4763)