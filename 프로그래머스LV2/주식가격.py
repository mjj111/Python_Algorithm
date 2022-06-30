from collections import deque
def solution(prices):
    tmpPrice = deque(prices)
    answer = []
    while tmpPrice:
        price = tmpPrice.popleft()
        sec = 0
        for q in tmpPrice:
            sec += 1
            if price > q:
                break 
        answer.append(sec)        
    return answer