def solution(s):
    answer = ''
    
    mok, namo = divmod(len(s),2)
    if namo == 0: # 짝수
        answer = s[mok-1:mok+1]
    else: # 홀수
        answer = s[mok]
        
    return answer