import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []

shark = deque()
for i in range(n):
    temp = list(map(int, input().split()))
    for t in range(m):
        if temp[t] == 1:
            shark.append((i,t)) #상어의 주소값 shark에 저장 
    arr.append(temp)# 상어가 담긴 수족관 

mx = [-1, -1, -1, 0, 1, 0, 1, 1]
my = [-1, 0, 1, 1, 1, -1, 0, -1]


def bfs():
    while shark: #상어를 기준으로 계속 돌려서 확인할 것이니까 
        x, y = shark.popleft()
        for k in range(8):
            dx = x + mx[k]
            dy = y + my[k]
            if 0 <= dx < n and 0 <= dy < m:
                if arr[dx][dy] == 0:
                    shark.append((dx,dy))
                    arr[dx][dy] = arr[x][y] + 1
    return


bfs()
safe_dist = 0
for i in range(n):
    for j in range(m):
        safe_dist = max(safe_dist, arr[i][j])

print(safe_dist - 1)