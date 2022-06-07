dx=[-1,0,1,0]
dy=[0,1,0,-1]
n=int(input())
list_=[list(input()) for _ in range(n)]
apt=[]

def dfs(x,y):
    global cnt
    list_[x][y] = '0'
    cnt+=1
    for i in range(4):
        nx = x + dx[i] 
        ny = y + dy[i]
        if nx < 0 or nx >= n or ny < 0 or ny >=n:
            continue
        if list_[nx][ny] == '1':
            dfs(nx,ny)

for i in range(n):
    for j in range(n):
        if list_[i][j] == '1':
            cnt= 0
            dfs(i,j)
            apt.append(cnt)

print(len(apt))
apt.sort()
for i in apt:
    print(i)