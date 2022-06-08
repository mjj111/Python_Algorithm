import sys
sys.setrecursionlimit(1000000)
global num
num = [9,8,7,6,5,4,3,2,1,0]
 
digit = 2
temp = [0 for i in range(2)]
global ans
ans =[]
i=0
def dfs(arr,digit,depth):
    global num
    global ans
    if depth == digit:
        t=0
        while digit>0:
            t+=arr[len(arr)-digit]*10**(digit-1)
            digit-=1
        ans.append(t)
        return
    for i in range(num.index(arr[depth-1])+1,10-(digit-depth)+1):
        arr[depth]=num[i]
        dfs(arr.copy(),digit,depth+1)
 
n = int(input())
if n >= 1023:
    print(-1)
else:
    for digit in range(1,11):
        arr = [0 for i in range(digit)]
        for i in range(10-digit+1):
            arr[0]=num[i]
            dfs(arr,digit,1)
        if len(ans) >= n+1:
            break
    ans.sort()
    print(ans[n])
