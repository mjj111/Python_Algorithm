n = int(input())
graph = []
num = []

for i in range(n):
    graph.append(list(map(int, input())))
Ax,Ay = map(int,input().split())

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]


def DFS(x, y):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        global count
        count += 1
        graph[x][y] = 0
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            DFS(nx, ny)
        return True
    return False


count = 0
if DFS(Ax,Ay) == True:
    print(count)
else:
    print(-1)
