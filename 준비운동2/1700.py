# 플러그를 꼽을 건데 빈공간이 있을 때까지 순서대로 계속 넣을 것이다.
# 남은 녀석들 중 이미 플러그에 있는 녀석이 있다면 그 플러그는 빼지 않는다.
# 남은 녀석들 중 현재 플러그에 없다면 
# 현재 플러그씩 찾아서 만나게될 녀석들의 인덱스 중 가장 멀리있는 플러그를 뺀다
# //현재 플러그의 남은녀석들의 갯수가 최대라면x 이런식으로 하면 안된다.
import sys
input = sys.stdin.readline
N, K = map(int, input().split())
use = list(map(int, input().split()))

plugs = []
result = 0
for i in range(K):
    # 이미 있다면
    if use[i] in plugs:
        continue

    # 빈공간이 있다면
    if len(plugs) != N:
        plugs.append(use[i])
        continue

    # 가장 멀리 있는 플러그의 인덱스
    far_one = 0
    temp = 0
    # 현재 꽂혀있는 플러그들 확인
    for plug in plugs:
        # 앞으로 사용할 플러그에 없으면
        if plug not in use[i:]:
            temp = plug
            break
        # 현재까지 가장 멀리 있는 플러그보다 멀리 있으면
        elif use[i:].index(plug) > far_one:
            far_one = use[i:].index(plug)
            temp = plug
    plugs[plugs.index(temp)] = use[i]
    result += 1
print(result)