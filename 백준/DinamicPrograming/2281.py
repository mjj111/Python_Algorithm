n,m = map(int,input().split())
arr = []
for i in range(n):
    arr.append(int(input()))

#dp[i][j]는 i번째 이름을 쓰고 j 여유공간이 있고 남은 공간의 제곱값 
dp = [-1 for i in range(1001)]*(1001)
def dfs(idx,rem):
    if(idx == n):
        return 0
    if dp[idx][rem] != -1:
        return dp[idx][rem]
    dp[idx][rem] = rem**2 + dfs(idx+1,m-arr[idx]%m)
    if(rem >=2):
        if rem == m:
            dp[idx][rem] = min(dp[idx][rem],dfs(idx+1,m-arr[idx]%m))
        elif rem>= arr[idx]+1 :
            dp[idx][rem] = min(dp[idx][rem], dfs(idx+1,rem - (arr[idx]+1)))
    return dp[idx][rem]
print(dfs(0,m))