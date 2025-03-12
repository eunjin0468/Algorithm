n,m = map(int, input().split())
truth = set(input().split()[1:])
party = []

for _ in range(m):
    party.append(set(input().split()[1:]))

for _ in range(m):
    for p in party:
        if p&truth:
            truth = truth.union(p)

cnt = 0
for p in party:
    if truth&p:
        continue
    else:
        cnt+=1
print(cnt)