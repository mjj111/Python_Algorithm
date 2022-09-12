from collections import deque
queue=deque()
queue.append([0,0])
cnt=0
dy=[-1,0,1,0]
dx=[0,1,0,-1]

def bfs(y,x,start):
    visited[y][x]=start
    queue.append([y,x])
    while queue:
        qy,qx=queue.popleft()
        for i in range(4):
            my=qy+dy[i]
            mx=qx+dx[i]
            if my<0 or my>=n or mx<0 or mx>=m:
                continue
            if data[my][mx]==1 and visited[my][mx]==0:
                visited[my][mx]=visited[qy][qx]+1
                queue.append([my,mx])
            if my==n-1 and mx==m-1:
                return
bfs(0,0,1)