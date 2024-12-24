a = int(input())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
cnt=0
for i in range(a):
    if arr2[i]>=arr1[i]:
        cnt+=1
print(cnt)