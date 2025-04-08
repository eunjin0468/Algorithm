import sys
input = sys.stdin.readline

str_a = ' '+input().rstrip()
str_b = ' '+input().rstrip()

dp = [[0]*len(str_b) for _ in range(len(str_a))]

for i in range(1, len(str_a)):
    for j in range(1, len(str_b)):
        if str_a[i] == str_b[j]:
            dp[i][j] = dp[i-1][j-1]+1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
print(dp[-1][-1])