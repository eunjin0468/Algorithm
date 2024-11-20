n = int(input())
arr = list(map(int, input().split()))
arr.sort(reverse=True)
list=[]
for i in range(len(arr)):
    list.append(arr[i]+i+1)
print(max(list)+1)