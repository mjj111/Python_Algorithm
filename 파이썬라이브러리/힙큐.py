import heapq

h = []
heapq.heapify(h) # 기존에 존재하는 h라는 배열을 heap으로 만듦
heapq.heappush(h, i) # i라는 원소 힙에 삽입. O(logN) 소요.
heapq.heappop(h) # 가장 작은 값을 가진 루트 노드 리턴. O(logN) 소요.
h[0] # 삭제하지 않고 루트 노드의 값만 읽어 오기
import heapq

def heapsort(h):
    heapq.heapify(h)
    sorted_arr = []
    while len(h) > 0:
        sorted_arr.append(heapq.heappop(h))
    return sorted_arr