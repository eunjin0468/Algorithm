import sys
def rou(num):
        if num - int(num) >= 0.5:
            return int(num)+1
        else:
            return int(num)
n = int(sys.stdin.readline())
if not n:
    print(0)
else:
    m = rou(n*0.15)
    arr = sorted([int(sys.stdin.readline()) for _ in range(n)])
    arr1 = arr[m:n-m]
    avg = rou(sum(arr1)/len(arr1))
    print(avg)