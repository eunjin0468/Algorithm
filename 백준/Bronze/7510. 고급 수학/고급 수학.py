t = int(input().strip())
for i in range(1,t+1):
    arr = list(map(int, input().split()))
    arr.sort()
    print(f"Scenario #{i}:")
    if arr[0]**2+arr[1]**2==arr[2]**2:
        print("yes\n")
    else:
        print("no\n")