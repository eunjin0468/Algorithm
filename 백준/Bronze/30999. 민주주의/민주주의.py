a,b = map(int, input().split())
result = 0
for _ in range(a):
    arr = []
    d = input()
    if d.count('O')>(b/2):
        result+=1
print(result)