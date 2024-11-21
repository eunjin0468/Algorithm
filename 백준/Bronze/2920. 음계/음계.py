arr = list(map(int, input().split()))
flag = False
if arr == sorted(arr):
    print("ascending")
elif arr == sorted(arr, reverse=True):
    print("descending")
else:
    print("mixed")