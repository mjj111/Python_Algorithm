#? 어쩌다보니 10분 컷
def solution(priorities, location):
    answer = 0
    # 모든 인덱스에서 최대 우선순위를 갖는 요소들을 찾아줄 것이다. 
    # 찾을 때 마다 answer += 1 하여 location에 해당하는 요소가 언제 출력되는지 확인 할 수있다.
    while(True):
        maxPrinter = max(priorities)
        for i in range(len(priorities)):
            if priorities[i] == maxPrinter: # 가장 큰 녀석을 찾았다
                answer+=1
                priorities[i] = 0
                maxPrinter = max(priorities)
                if i == location:
                    return answer