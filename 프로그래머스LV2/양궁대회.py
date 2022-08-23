import copy

def solution(n, info):
    answer = [0 for i in range(11)]
    max_,apeachScore  = 0,0
    
    for i in range(len(info)):
        if info[i] != 0:  apeachScore += 10-i
    
    def dfs(apeachScore,lionScore,arrow,count,li):
        temp = copy.deepcopy(li)
        if count>=11 or arrow==0:  
            nonlocal max_
            nonlocal answer
            if arrow > 0:   temp[-1]=arrow
            if max_ < lionScore - apeachScore : 
                if arrow>0: answer[-1] = arrow
                max_ = lionScore - apeachScore
                answer = temp
            elif max_ == lionScore - apeachScore:
                a,b = 0,0
                for i in range(11):
                    if answer[i]:   a+=i
                    if temp[i]: b+=i
                if b>=a: answer = temp
            return
        else:
            # 넘기기
            dfs(apeachScore,lionScore,arrow,count+1,temp)
            #어피치보다 많이 쏘기
            if arrow-info[count]-1 >=0 and info[count] != 0:
                temp[count] = info[count] + 1
                dfs(apeachScore-(10-count),lionScore+(10-count),arrow-info[count]-1,count+1,temp)
            elif info[count] == 0:    #어피치가 안 쏜것
                lionScore += 10 - count
                temp[count] = 1
                dfs(apeachScore,lionScore,arrow-info[count]-1,count+1,temp)
    dfs(apeachScore,0,n,0,answer)
    return answer if answer != [0,0,0,0,0,0,0,0,0,0,0] and  max_ !=0  else [-1]