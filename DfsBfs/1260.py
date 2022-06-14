from collections import deque


def dfs(v): #재귀 사용
    print(v,end = ' ')
    visit[v] = 1
    for i in range(1,n+1):
        if visit[i] == 0 and s[v][i]==1:
            dfs(i)

def bfs(v): # deque() 사용 
    queue = deque()
    queue.append(v)
    visit[v] = 0
    while(queue):
        v = queue.popleft()
        print(v, end =' ')
        for i in range(1,n+1):
            if visit[i] == 1 and s[v][i] == 1:
                queue.append(i)
                visit[i] = 0

n, m, v = map(int, input().split())
s = [[0] * (n + 1) for i in range(n + 1)] # s[i][j] 는 i에서 j를 향한 노드가 있다면 1이다.
visit = [0 for i in range(n + 1)] # 어떤 노드에서 visited[i] i 에 간적이 있는가 없는가에 대한 리스트.
for i in range(m):
    x, y = map(int, input().split())
    s[x][y] = 1
    s[y][x] = 1
    
dfs(v)
print()
bfs(v)