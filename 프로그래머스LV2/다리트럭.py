def solution(bridge_length, weight, truck_weights):
    answer = 0
    bridge = [0 for i in range(bridge_length)] # 지나갈 다리 초기화
    while bridge: # 다리를 파괴 및 수복의 과장을 거쳐 마지막에 bridge는 소멸될 것이다. 
        bridge.pop(0)
        answer+=1
        if truck_weights: # 해당 리스트도 삭제해줄 것이다. 
            if truck_weights[0] + sum(bridge) <= weight:# 탑승 가능 시
                bridge.append(truck_weights.pop(0))
            else:
                bridge.append(0)
    return answer