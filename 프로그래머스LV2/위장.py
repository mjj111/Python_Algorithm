def solution(clothes):
    answer = 0
    dic ={}
    tmpsum =1
    for i in clothes:
        dic[i[1]] = dic.get(i[1],0) + 1
    for i in dic.values():
        tmpsum*=i+1 # 각 요소들의 값이 쓰이지 않을 수도 있는 경우가 있으니 +1 해서 곱해준다. 약수 개수 구하는 것과 같다.
    answer= tmpsum -1 # 그러나 모두 다 안쓸 수 있는 경우의 수를 제거 -1 
    return answer