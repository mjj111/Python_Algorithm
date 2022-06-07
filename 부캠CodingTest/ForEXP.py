import sys

input = sys.stdin.readline
n = int(input())
num = list(map(int,input().split()))
op = list(map(int,input().split())) # 연산식 +, -, *, //

maximum =-1e9
minimum =1e9

def dfs(depth,total,plus,minus,multiply,divide):
    global maximum,minimum
    if depth == n:
        maximum = max(maximum,total)
        minimum = min(minimum,total)
        return
    
    if plus : 
        dfs(depth+1,total + num[depth],plus-1,minus,multiply,divide)
    