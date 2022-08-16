from collections import deque 
def solution(order):
    # 크기가 모두 같으면 1~n 오름차순 영재에게 전달 
    # 1번부터 내린다.
    # 만약 배달 순서가 아니라면 다른 곳에 보관
    # 다른 곳은 stack 구조
    # 만약 배달 순으로 못 내린다면 더 이상 상자를 안실어
    # return 실을 수 있는 택배 개수
    answer = 0
    arr = deque(order)
    stack = []
    flag = True
    for i in range(1,len(order)+1):
        if i == arr[0]:
            arr.popleft()
            answer+=1
        elif stack and arr[0] == stack[-1] :
            stack.pop()
            arr.popleft()
            answer+=1
            stack.append(i)
            while stack:
                if arr[0] == stack[-1]:
                    stack.pop()
                    arr.popleft()
                    answer+=1
                else:
                    break
        else:
            stack.append(i)
    while(stack):
        if arr[0]== stack[-1]:
            answer+=1
            stack.pop()
            arr.popleft()
        else:
            break
    return answer