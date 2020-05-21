import heapq

def solution(scoville, K):
    count = 0
    heapq.heapify(scoville)
    while scoville[0] < K:
        if len(scoville) == 1:
            return - 1
        a = heapq.heappop(scoville)
        b = heapq.heappop(scoville)
        heapq.heappush(scoville, a + (b * 2))
        count += 1
    return count

if __name__ == '__main__':
    answer = solution([1, 2, 3, 9, 10, 12], 7)
    print(answer)   # 2
    answer = solution([12, 7, 6, 3, 2, 1], 3)
    print(answer)   # 1
    answer = solution([9, 2, 3], 26)
    print(answer)   # 2