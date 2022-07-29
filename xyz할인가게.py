def solution(want, number, discount):
    answer = 0
    # 10일 회원(일정금액 이상)
    # 한가지 할인 (하루 하나)
    # 원하는 제품,수량 할인날짜, 10일 연속에 속하면 회원가입
    # return 모두 구매가 가능한 회원등록 날짜 총 일수 
    dic = {}
    tmpd = {}
    for i in range(len(want)):
        dic[want[i]] = number[i]
    for j in range(len(discount) - 9):
        for i in range(10):
            tmpd[discount[j + i]] = tmpd.get(discount[j+ i],0) + 1
        if dic == tmpd:
            answer +=1
            tmpd.clear()
        else:
            tmpd.clear() 
    return answer
want = ["banana", "apple", "rice", "pork", "pot"]
number = [3, 2, 2, 2, 1]
discount = ["chicken", "apple", "apple", "banana", "rice", "apple", "pork", "banana", "pork", "rice", "pot", "banana", "apple", "banana"]
print(solution(want,number,discount))