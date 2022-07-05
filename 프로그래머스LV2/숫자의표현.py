def solution(n):
    answer = 0
    for i in range(1, 140): 
        if n < i + sum(range(i)): break 
        if (n-sum(range(i)))/i == int((n-sum(range(i)))/i): 
            answer += 1
    return answer