str = input().upper()
arr = list(set(str))
result = []
for i in arr:
    result.append(str.count(i))
if result.count(max(result))>1:
    print("?")
else:
    print(arr[result.index(max(result))])