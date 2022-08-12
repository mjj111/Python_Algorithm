import math
def timeCal(a,b):
    a= list(map(int, a.split(':')))
    b= list(map(int, b.split(':')))
    
    h = a[0] - b[0]
    if a[1] < b[1]:
        h -= 1
        m = a[1] + 60 - b[1]
    else:   m = a[1] - b[1]
    return  h*60 + m
        
   
def fee(time,fees):
    if time <= fees[0]: return fees[1]
    else:
        time -= fees[0]
        return fees[1] + math.ceil(time/fees[2]) * fees[-1]


def solution(fees, records):
    answer = []
    recordsDic = {}
    
    for r in records:
        temp = r.split()
        if temp[1] in recordsDic:   recordsDic[temp[1]].append(temp[0])
        else:   recordsDic[temp[1]] = [temp[0]]
    
    recordsDic = sorted(recordsDic.items()) 
    for car,time in recordsDic:
        if len(time) % 2 == 1: time.append('23:59')
        tempTime = 0 
        while time:
            a = time.pop()
            b = time.pop()
            tempTime += timeCal(a,b)
        answer.append(fee(tempTime,fees))
    return answer