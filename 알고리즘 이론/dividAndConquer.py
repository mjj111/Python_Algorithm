# 6549 BOJ
import sys

def divdeandconquer(a):
    if len(a) == 1:
        return a[0]
    if len(a) % 2 == 1: # 홀수일 떄
        a = [0] + a #히스토그램에 0을 하나 넣어준다.
    d = len(a) // 2 #중앙
    x = a[:d] # 중앙에서 좌
    y = a[d:] # 중앙에서 우
    cnt = 2
    tmpmax = min(a[d - 1], a[d]) # 중앙혹은 중앙 전값 중에 가장 작은 값 = tmamax
    tmparea = tmpmax * cnt # 중앙선을 포함한 직사각형의 넓이
    i = 0
    j = 0
    for _ in range(0, len(a) - 2):
        if d - 1 - i == 0: # i를 더 이상 못움직일 떄 
            j += 1
        elif d + j == len(a) - 1: # j를 더 이상 못 움직일 떄 
            i += 1
        else: # i,j가 범위안에 있다. 
            if a[d - 2 - i] >= a[d + 1 + j]: # 왼족에 녀석 높이가 오른쪽 보다 이상 일때 
                i += 1 # 밑변을 왼쪽으로 옮긴다. 
            else:
                j += 1 # 밑변을 오쪽으로 옮긴다. 
        tmpmax = min(tmpmax, a[d - 1 - i], a[d + j]) # 가장 작은 값을 높이로 두고 
        cnt += 1 # 밑변 길이를 만들어 
        tmparea = max(tmparea, tmpmax * cnt) # 넓이 비교 
    z = tmparea
    return max(divdeandconquer(x), divdeandconquer(y), z)

while True : #입력
    n, histogram = list(map(int, sys.stdin.readline().split()))
    if n == 0:
        break
    maxarea = divdeandconquer(histogram)
    print(maxarea)