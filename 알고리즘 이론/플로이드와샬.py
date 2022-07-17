import sys
input = sys.stdin.readline

N = int(input().rstrip())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]

for k in range(0, N):         # 경유지 노드
    for i in range(0, N):     # 출발 노드
        for j in range(0, N): # 도착 노드
            if matrix[i][k]==1 and matrix[k][j]==1:
                matrix[i][j] = 1


for m in matrix:
    print(*m)