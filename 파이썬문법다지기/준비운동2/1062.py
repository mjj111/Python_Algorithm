# 가르침
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
arr = []
for _ in range(N):
    arr.append(input().strip()) # 인자가 없을 경우 왼쪽 공백 제거
alpha = ['a', 'n', 't', 'i', 'c']
alpha_list = ['b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm',
              'o', 'p', 'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']


def choose_alpha(n, start):
    global result
    if n == 0:
        result = max(result, check())
        return
    for i in range(start, len(alpha_list)): #하지만 예술은 시작된다. 현재 새로운 녀석을 추가 후, 다시 재귀(글자 수-1, 시작할 인덱스+1)을 넣어준다.
        alpha.append(alpha_list[i])
        choose_alpha(n-1, i+1)
        alpha.pop()


def check():# 체크만 하면된다.
    result = 0
    for words in arr:
        isRead = True
        for i in range(4, len(words)-4):
            if words[i] not in alpha:
                isRead = False
                break
        if isRead:
            result += 1
    return result


result = 0
if K < 5:
    print(result)
else:
    choose_alpha(K-5, 0)
    print(result)