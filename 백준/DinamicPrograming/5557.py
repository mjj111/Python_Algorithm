import sys
input = sys.stdin.readline
n = int(input())
arr = list(map(int, input().split()))
last = arr[-1]
dp = [[0] * 21 for i in range(n)] # dp[i][j] 는 i번째 연산에서 j의 값을 갖고있는 경우의수의 갯수
dp[0][arr[0]] = 1
for i in range(1, n - 1):
    for j in range(21):
        if dp[i - 1][j]:
            if 0 <= j + arr[i] <= 20:
                dp[i][j + arr[i]] += dp[i - 1][j]
            if 0 <= j - arr[i] <= 20: 
                dp[i][j - arr[i]] += dp[i - 1][j]
print(dp[n - 2][last])