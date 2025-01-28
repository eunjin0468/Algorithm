n = int(input())
L = [0] + list(map(int, input().split()))
H = [0] + list(map(int, input().split()))
dp = [[0]*101 for _ in range(n+1)]
for i in range(1, n+1):
    l, h = L[i], H[i]
    for j in range(1, 101):
        if j < l: #기쁨<체력
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-l]+h) #max(이전활동, 이전활동+현재행복)
print(dp[n][99])