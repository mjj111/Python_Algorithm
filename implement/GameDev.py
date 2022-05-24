n,m = map(int,input().split())
d = [ [0]*m for _ in range(n)]
x,y,direction = map(int,input().split())
d[x][y] = 1

arr = []
for i in range(n):
    arr.append(list(map(int,input().split())))
dx = [-1,0,1,0]
dy = [0,1,-0,-1]

def turnLeft():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

count = 1
turnTime = 0
while True:
    turnLeft()
    nx = x + dx[direction]
    ny = y + dy[direction]
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        y= ny
        x= nx
        count +=1
        turnTime = 0
        continue
    else:
        turnTime +=1
    if turnTime == 4 :
        nx = x - dx[direction]
        ny = y - dy[direction]
        if arr[nx][ny] ==0:
            x = nx
            y = ny
        else:
            break
        turnTime = 0
print(count)