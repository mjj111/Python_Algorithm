from collections import deque
 
A, B = map(int, input().split())
 
q = deque()
q.append((A, 1))
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