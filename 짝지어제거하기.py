# for 문을 두개 이상 돌릴 시 10억을 넘기에 for 한개에서 해결해야했던 문제 
#스택에 가장 최근 녀석과 현재 진행하는 녀석을 비교해줘야한다. 
# 다 돌린 뒤에 스택에 뭔가 있다면? -> 다 없애지 못하는 녀석 
def solution(s):
    if len(s) % 2 == 1: return 0 
    if len(s) == 2: 
        return 1 if s[0] == s[1] else 0
            
    stack = [s[0]]
    
    for v in s[1:]:
        if stack and stack[-1] == v:
            stack.pop()
        else:
            stack.append(v)
            
    return 0 if stack else 1