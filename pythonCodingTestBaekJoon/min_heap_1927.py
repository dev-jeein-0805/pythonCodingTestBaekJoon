# 1927 최소 힙

import heapq

N = int(input())
first_list = []

# N 개의 요소를 리스트에 담고, 0 의 개수를 count() 함수 사용해서 zeroCount 에 저장
for _ in range(N):
    first_list.append(int(input()))
zeroCount = first_list.count(0)

min_heap = []

output = []
idx = 0  # first_list를 순회하기 위한 인덱스
# 위에서 저장한 0 의 개수(=zeroCount) 만큼 for문 순회
for _ in range(zeroCount):
    while idx < len(first_list):
        x = first_list[idx]
        idx += 1
        if x > 0:
            heapq.heappush(min_heap, x)
        elif x == 0:
	    # min_heap 에 요소가 있을 때
            if min_heap:
                smallest = heapq.heappop(min_heap)
                output.append(smallest)
            # min_heap 이 빈 [] 일 때
            else:
                output.append(0)

for value in output:
    print(value)
