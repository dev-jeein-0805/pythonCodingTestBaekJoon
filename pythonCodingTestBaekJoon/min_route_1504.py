# 1504 특정한 최단 경로

# 특정 두 정점을 반드시 거쳐야 하는 최단 경로를 구하는 문제

import heapq
import sys
input = sys.stdin.readline
INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정. 최단 거리를 초기화

v, e = map(int, input().split()) # v: 정점의 개수, e: 간선의 개수
graph = [[] for _ in range(v + 1)] # 인접 리스트로 그래프를 표현. 정점 번호가 1부터 시작하므로 v + 1 크기로 초기화

# 방향성 없는(=양방향) 그래프이므로 x, y일 때와 y, x일 때 모두 추가
for _ in range(e):
    x, y, cost = map(int, input().split())
    graph[x].append((y, cost))
    graph[y].append((x, cost))

# dijkstra(start): 시작 정점 start로부터 모든 정점까지의 최단 거리를 계산하여 반환
# distance: 각 정점까지의 최단 거리를 저장하는 리스트
# 우선순위 큐를 사용하여 현재 가장 짧은 거리를 가진 정점을 선택하고, 그 정점으로부터 인접한 정점까지의 거리를 업데이트함
def dijkstra(start):
    distance = [INF] * (v + 1)
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for i in graph[now]:
            cost = dist + i[1]

            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

    # 반환값은 최단 거리 배열
    return distance

v1, v2 = map(int, input().split()) # v1, v2: 경유해야 하는 두 정점

# 출발점이 각각 1, v1, v2일 때의 최단 거리 배열
original_distance = dijkstra(1) # 시작점 1로부터 각 정점까지의 최단 거리 배열
v1_distance = dijkstra(v1) # v1로부터 각 정점까지의 최단 거리 배열
v2_distance = dijkstra(v2) # v2로부터 각 정점까지의 최단 거리 배열

v1_path = original_distance[v1] + v1_distance[v2] + v2_distance[v] # 1 -> v1 -> v2 -> v 경로의 총 비용
v2_path = original_distance[v2] + v2_distance[v1] + v1_distance[v] # 1 -> v2 -> v1 -> v 경로의 총 비용

result = min(v1_path, v2_path) # 두 경로 중 더 짧은 경로의 비용 저장
print(result if result < INF else -1) # 만약 경로가 존재하지 않을 경우 -1을 출력
