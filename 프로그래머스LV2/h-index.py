def solution(citations):
    answer = 0
    citations.sort()
    maxNum = 0
    for i in range(len(citations)):
        if citations[i] <= len(citations)-i: # h번 이상 인용된 논문이 h편 이상 
            return len(citations)-i
    return 0