from collections import deque
 
A, B = map(int, input().split()) # 가장 중요한 점은 B 보다 클 경우 더 이상의 연산이 필요하지 않다는 것이다
 
q = deque()
q.append([A, 1]) #현재수, 실행 수
s =1 
 
while q:
    x, t = q.popleft()
    if x == B:
        print(t)
        s= 2
        break
 
    if x*2 <= B:
        q.append((x*2, t+1))
    x = int(str(x) + "1")
    
    if x <= B:
        q.append((x, t+1))
if s == 1:
    print(-1)