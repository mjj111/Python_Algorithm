import sys
from heapq import heappush, heappop
input = sys.stdin.readline
n = int(input())
m = int(input())
inf = 100000000
s = [[] for i in range(n + 1)] # s[a] = [b,c] 는 a에서 b를 향한 c가치 값이다.
dp = [inf for i in range(n + 1)] #dp[a]는 start에서 a노드까지 가는 누적 가치값이다.

for i in range(m):
    a, b, w = map(int, input().split())
    s[a].append([b, w])
start, end = map(int, input().split())


def dijkstra(start):
    #기본적으로 bfs의 코드틀을 갖고있다. 
    dp[start] = 0 # 자기자신은 0으로 시작
    heap = [] # 돌릴 애들을 heap 선언
    heappush(heap, [0, start])
    while heap:
        w, n = heappop(heap)
        if dp[n] < w: # n까지가는 비용이 현재 녀석의 비용보다 작다면 실행하지 않는다.// 나머지 불필요한 애들 거르기 위해 사용 
            continue
        for n_n, wei in s[n]: # n 에 연결된 노드를 꺼내서 비용에 가중하여 저장해준다.
            n_w = w + wei
            if n_w < dp[n_n]: #만약 꺼낸 다음 노드의 비용이 저장된 다음 노드의 값보다 적다면!(아직 안갔으니까) 효율적이므로 heap에 넣어준다.
                dp[n_n] = n_w # 다음 노드의 값을 저장
                heappush(heap, [n_w, n_n])
dijkstra(start)
print(dp[end])