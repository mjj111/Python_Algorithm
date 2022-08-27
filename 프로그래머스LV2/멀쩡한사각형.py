import math

def solution(w,h):
    answer = 0
    start = 0
    if w == h:
        return w*h - h
    if w > h:
        w, h = h, w
    temp = h / w
    for i in range(w):
        pre = start #이전꺼
        start += temp #더한거
        print(math.ceil(start), int(pre))
        if math.ceil(start) != int(pre): #더한거 올림한거랑 이전꺼 내림한거랑 다르면
            answer += math.ceil(start) - int(pre) #올림 - 내림
        else:
            answer += 1 #같으면 1개
    return w*h - answer