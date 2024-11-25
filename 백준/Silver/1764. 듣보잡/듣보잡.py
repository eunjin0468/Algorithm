n,m = map(int, input().split())
a,b,result = set(), set(),[]
for _ in range(n):
    a.add(input())
for _ in range(m):
    b.add(input())
for i in a:
    if i in b:
        result.append(i)
result.sort()
print(len(result))
print('\n'.join(result))