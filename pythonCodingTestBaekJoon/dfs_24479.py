# 24479 알고리즘 수업 - 깊이 우선 탐색 1

# 깊이 우선 탐색(DFS)
def dfs(t):
    global cnt # 방문 순서를 기록
    visited[t] = cnt
    line[t].sort() # 인접 노드들 오름차순 정렬
    for i in line[t]:
        if visited[i] == 0:
            cnt += 1
            dfs(i) # 재귀적 호출

import sys
sys.setrecursionlimit(150000) # 재귀 호출의 최대 깊이 설정
N, M, R = map(int, sys.stdin.readline().split()) # N: 노드 개수, M: 간선 개수, R: 시작 노드
line = [[] for _ in range(N+1)] # 각 노드는 인접 노드 목록 가짐
visited = [0]*(N+1)  # 각 노드의 방문 순서를 기록
cnt = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().split()) # 각 간선을 입력 받아 그래프를 구성
    line[a].append(b)  # 양 방향 간선 처리 (a 와 b 서로 연결됨)
    line[b].append(a)  # 양 방향 간선 처리 (a 와 b 서로 연결됨)

dfs(R) # 시작 노드 R 에서 dfs 호출

for i in range(1, N+1):
    print(visited[i]) # 각 노드의 방문 순서 출력

# DFS 우선 좀더 공부가 필요하여 공유된 코드에서 한 줄 씩 해석한 것으로 먼저 공부하였다.
