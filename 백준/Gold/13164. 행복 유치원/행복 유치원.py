a,b = map(int, input().split())
arr = list(map(int, input().split()))
kids = []
for i in range(1, a):
    kids.append(arr[i]-arr[i-1])
kids.sort(reverse=True)
print(sum(kids[b-1:]))