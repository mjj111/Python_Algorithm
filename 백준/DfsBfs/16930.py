from collections import deque
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
N, M, K = map(int, input().split()) # N:세로 M:가로, K: step
D = [list(input()) for _ in range(N)] # 움직일 맵
sx, sy, ex, ey = map(int, input().split())
sx -= 1; sy -= 1; ex -= 1; ey -=1 # n만큼 만들었기 떄문에 맞는 인덱스를 갖기위해 하나씩 뺴줬다.
check = [[float('inf')]*M for _ in range(N)] # 방문 맵 (inf로 둬야만 최소값을 출력한다)
q = deque()
q.append((sx, sy))
check[sx][sy] = 0 #시작점 초기화
 
while q:
    x, y = q.popleft()
    for i in range(4):
        nx, ny = x + dx[i], y + dy[i]
        nk = 1 # 출발 k까지 움직일 수가 있다. 
        while nk <= K and 0 <= nx < N and 0 <= ny < M and D[nx][ny] != '#' and check[nx][ny] > check[x][y]:
            if check[nx][ny] == float('inf'):
                q.append((nx, ny)) # 새롭게 출발 가능 
                check[nx][ny] = check[x][y] + 1
            nx += dx[i]
            ny += dy[i]
            nk += 1 #같은 방향으로 계속 가는 중
if check[ex][ey] == float('inf'):
    print(-1)
else:
    print(check[ex][ey])