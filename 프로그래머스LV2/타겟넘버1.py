def solution(numbers, target):
    n= len(numbers)
    count= 0
    
    def dfs(temp, idx):
        if idx >=n:
            if temp == target: 
                nonlocal count
                count+=1
            return 
        else:
            dfs(temp+numbers[idx],idx+1)
            dfs(temp-numbers[idx],idx+1)
    
    dfs(0,0)
    return count