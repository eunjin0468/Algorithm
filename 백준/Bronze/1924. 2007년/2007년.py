a,b = map(int, input().split())
day = ["SUN", "MON", "TUE", "WED", "THU", "FRI", "SAT"]
arr = [31,28,31,30,31,30,31,31,30,31,30,31]
cnt = 0
for i in range(a-1):
    cnt+=arr[i]
cnt = (cnt+b)%7
print(day[cnt])