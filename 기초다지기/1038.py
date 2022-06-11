N = int(input())
answer = -1
def dfs(k, nums):
    global answer
    if len(nums) == k:
            answer += 1
            if answer == N:
                print(nums)
                exit(0)
    else:
        if nums == '':
            for j in range(k-1, 10): #맨 앞자리수는 아무거나 가능.
                dfs(k, str(j))
        else:
            for j in range(k-len(nums)-1, int(nums[-1])): 
                dfs(k, nums+str(j))

for i in range(1, 11): #0부터 9876543210의 경우 까지, 총 10자리수일때까지만 해당 수가 가능하다.
    dfs(i, '')

print('-1')