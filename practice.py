import sys
import heapq
INF = int(1e9)
n,m = map(int, input().split())
distance = [INF]*(n+1)
start = int(input())
graph = [[] for _ in range(n+1)]
for i in range(m):
    a,b,c = map(int,input().split()) # b는 다음녀석 c는 cost
    graph[a].append([b,c])

def dijkstra(start):
    q = []
    heapq.heappush(q,[0,start])
    distance[start] = 0 
    while q :
        tmpcost, nodeIdx =heapq.heappop(q)
        if tmpcost > distance[nodeIdx]:
            continue
        for i in graph[nodeIdx]:
            NextCost = distance[nodeIdx] + i[1]
            if NextCost < distance[i[0]]:
                distance[i[0]] = NextCost
                heapq.heappush(q,[NextCost,i[0]])
                
dijkstra(start)
for i in range(1, len(distance)):
    if distance[i] == INF:
        print('도달할 수 없음')
    else:
        print(distance[i])
             
# n 노드갯수 m 간선 갯수 3개값으로 받을 것 