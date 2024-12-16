arr = []
for i in range(8):
    arr.append((int(input()), i))
arr.sort(reverse=True)
cnt = 0
rank = []
for score, n in arr[:5]:
    cnt+=score
    rank.append(n+1)
print(cnt)
print(*sorted(rank))