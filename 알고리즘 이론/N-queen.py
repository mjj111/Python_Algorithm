def nqueen(sol, N):
    global count
    if len(sol) == N:  
        count += 1
        print(count, sol)
        return 0
    candidate = list(range(N))    
    for i in range(len(sol)):
        if sol[i] in candidate:  
            candidate.remove(sol[i])    
        distance = len(sol) - i     
        if sol[i] + distance in candidate:    
            candidate.remove(sol[i] + distance)       
        if sol[i] - distance in candidate:    
            candidate.remove(sol[i] - distance)      
    if candidate != []:
        for i in candidate:
            sol.append(i)   
            nqueen(sol, N)    
            sol.pop()
    else:    
        return 0 

count = 0
num = int(input())
for i in range(num):
    nqueen([i], num)
if count == 0:
    print("-1")
