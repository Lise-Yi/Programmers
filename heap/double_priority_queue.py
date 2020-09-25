import heapq

def solution(operations):
    heap = []
    for op in operations:
        if op[0] == "I":
            heapq.heappush(heap, int(op[2:]))
        else:
            if len(heap) == 0 : continue
            if op[2:] == "-1":
                heapq.heappop(heap)
            else:
                maxi = heapq.nlargest(1, heap)[0]
                heap.remove(maxi)
    if len(heap) == 0 : return [0,0]
    answer = heapq.nlargest(1, heap)
    answer.append(heap[0])
    return answer