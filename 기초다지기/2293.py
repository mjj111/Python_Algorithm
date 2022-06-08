n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1
# dp[i] -> i원을 만들 때 가능한 경우의 수
# dp[0] -> 동전 하나를 사용하는 경우 

for coin in coins:
    for i in range(coin, k+1):
        possible_cases = dp[i - coin]
        dp[i] += possible_cases

print(dp[k])