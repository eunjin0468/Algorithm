import sys

t = int(sys.stdin.readline())
for _ in range(t):
    k = int(sys.stdin.readline())

    file = [0] + list(map(int, sys.stdin.readline().split()))
    sum = [0] * (k + 1)
    for i in range(1, k + 1):
        sum[i] = sum[i - 1] + file[i]

    dp = list([0] * (k + 1) for _ in range(k + 1))
    for cnt in range(1, k):
        for start in range(1, k - cnt + 1):
            end = start + cnt

            MIN = sys.maxsize #정수형(int) 데이터의 최대 크기
            for mid in range(start, end):
                MIN = min(MIN, dp[start][mid] + dp[mid + 1][end])

            dp[start][end] = MIN + sum[end] - sum[start - 1]
            
    print(dp[1][k])