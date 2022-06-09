n= int(input())
# 다음 녀석을 미리 본다 
# 다음 녀석이 존재하면 그 녀석 위치로 간다 
# 그녀석의 위치 이전에서 그녀석 위치 까지의 값들중 가장 작은 값들을 저장해준다. 
# 끝까지 반복! -> 만약에 끝에 녀석이 inf라면 -1출력
n = int(input())
lst = input()

MAX = int(1e9)
dp = [MAX] * n

def get_prev(x):
    if x == "B":
        return "J"
    elif x == "O":
        return "B"
    elif x == "J":
        return "O"

dp[0] = 0
for i in range(1, n):
    prev = get_prev(lst[i])
    for j in range(i):
        if lst[j] == prev:
            dp[i] = min(dp[i], dp[j] + pow(i - j, 2))
print(dp[n - 1] if dp[n - 1] != MAX else -1)