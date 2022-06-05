from re import A
import sys 
input = sys.stdin.readline

r = 0
sum = 0

for i in range(10):
    n,m = map(int,input().split())
    sum -= n
    sum += m
    r = max(r,sum)
print(r)