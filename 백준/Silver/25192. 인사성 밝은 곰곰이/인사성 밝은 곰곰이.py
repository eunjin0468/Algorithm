n = int(input())
gom = set()
cnt = 0
for i in range(n):
    name = input()
    if name == "ENTER":
        cnt += len(gom)
        gom = set()
    else:
        gom.add(name)
print(cnt+len(gom))