import sys
input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
m = int(input())

#dp
dp = [[0] * n for _ in range(n)] #dp[i][j] 는 i부터 j까지의 숫자는 필란드룸이다 아니다를 가졌다. 


for num_len in range(n):
    for start in range(n - num_len):
        end = start + num_len
        

        if start == end:
            dp[start][end] = 1
        # 시작점의 글자와 끝점의 글자가 같다면
        elif numbers[start] == numbers[end]:
        	# 두 글자
            if start + 1 == end:
                dp[start][end] = 1
            # 가운데 문자 팰린드롬
            elif dp[start+1][end-1] == 1:
                dp[start][end] = 1
            

#정답출력하기
for question in range(m):
    s, e = map(int, input().split())
    print(dp[s-1][e-1])
