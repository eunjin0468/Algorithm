import sys


input = sys.stdin.read
data = input().splitlines()


a, b = map(int, data[0].split())

arr = [list(map(int, line.split())) for line in data[1:a+1]]


sum = [[0] * (a + 1) for _ in range(a + 1)]

for i in range(1, a + 1):
    for j in range(1, a + 1):
        sum[i][j] = arr[i - 1][j - 1] + sum[i - 1][j] + sum[i][j - 1] - sum[i - 1][j - 1]

result = []
for i in range(a + 1, a + 1 + b):
    x1, y1, x2, y2 = map(int, data[i].split())
    result.append(str(sum[x2][y2] - sum[x1 - 1][y2] - sum[x2][y1 - 1] + sum[x1 - 1][y1 - 1]))

sys.stdout.write("\n".join(result) + "\n")