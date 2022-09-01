#짝지어 제출하기
def solution(s):
    new = [[1,1]]
    s = list(s)
    for i in range(len(s)):
        if new[-1][0] != s[i]:
            new.append([s[i], 1])
        else:
            del new[-1]
    if len(new) == 1:
        return 1
    else:
        return 0