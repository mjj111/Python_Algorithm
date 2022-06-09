n, k = map(int, input().split())
thing = [[0,0]]
dp = [[0]*(k+1) for _ in range(n+1)] # dp[n][k]는 N번째 물건 까지 살펴보았을 때, 무게가 K인 배낭의 최대 가치 이다.
for i in range(n):
    thing.append(list(map(int, input().split())))

for i in range(1, n+1): #n개의 짐들 만큼 돌려줄 것이다. 
    for j in range(1, k+1):
        w = thing[i][0] # 무게
        v = thing[i][1] # 가치 

        #현재 담을 물건의 인덱스를 i, 현재 가방 허용 용량이 j, 현재 담을 물건의 무게를 weight, 가치 value라고 할 때,
        if j < w: 
            dp[i][j] = dp[i-1][j] 
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-w]+v)

print(dp[n][k])