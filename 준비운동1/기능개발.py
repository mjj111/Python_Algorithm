from collections import Counter
import math

def solution(progresses, speeds):
    answer = []
    queue = []
    for progress, speed in zip(progresses, speeds):
        queue.append(math.ceil((100 - progress) / speed))

    i = 0
    for j in range(1, len(queue)):
        if queue[j] < queue[i]:
            queue[j] = queue[i]
        i += 1

    count = Counter(queue).items()
    for item in count:
        answer.append(item[1])

    return answer


print(solution(	[93, 30, 55],  [1, 30, 5]))