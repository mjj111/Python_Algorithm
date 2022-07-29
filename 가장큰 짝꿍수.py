def solution(X, Y):
    answer = ''
    dic= {}
    arr = []
    for i in X:
        try:
            if dic[i] > 0:
                dic[i] = dic[i] + 1
        except:
            dic[i] = 1
    for j in Y:
        try :
            if dic[j] > 0:
                arr.append(j)
                dic[j] = dic[j] -  1
        except:
            continue
    
    if arr:
        arr.sort(reverse = True)
        if arr[0] == "0":
            return "0"
        for i in arr:
            answer+=i
    else:
        return "-1"
    return answer