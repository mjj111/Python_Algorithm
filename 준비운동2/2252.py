from collections import deque
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

n,m = map(int,input().split()) # n 학생을 받고 m만큼 비교연산
in_dgree = [0] *(n+1)
graph = [[]for i in range(n+1)] 

for i in range(m): # m 만큼 비교연산한다. 
    a, b = map(int,input().split())
    in_dgree[b] +=1  # a가 b보다 더 앞에 있어야하기에 b의 우선순위 +=1
    graph[a].append(b)
    
queue = deque()
ans = []

for i in range(1,n+1):
    if in_dgree[i] == 0:
        queue.append(i) #1등 시민들을 넣어준다.
        
while queue:
    current =queue.popleft()
    ans.append(current) #가장 괜찮은 우선순위 녀석들을 넣어준다.
    
    for x in graph[current]: # 현재 녀석의 다음으로 와도 되기에 한개 빼준다. 
        in_dgree[x] -=1
        
        if in_dgree[x] == 0 :# 근데 이녀석이 더 이상 기다릴 필요가 없다면 queue에 넣어준다. 
            queue.append(x)
            
print(*ans,end = " ")
#첫째 줄에 학생들을 앞에서부터 줄을 세운 결과를 출력한다. 답이 여러 가지인 경우에는 아무거나 출력한다.