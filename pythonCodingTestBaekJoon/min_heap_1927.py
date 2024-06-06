# 1927 최소 힙

import heapq

N = int(input())
first_list = []
for _ in range(N):
    first_list.append(int(input()))
zeroCount = first_list.count(0)

min_heap = []

output = []
idx = 0  # first_list를 순회하기 위한 인덱스
for _ in range(zeroCount):
    while idx < len(first_list):
        x = first_list[idx]
        idx += 1
        if x > 0:
            heapq.heappush(min_heap, x)
        elif x == 0:
            if min_heap:
                smallest = heapq.heappop(min_heap)
                output.append(smallest)
            else:
                output.append(0)

for value in output:
    print(value)
