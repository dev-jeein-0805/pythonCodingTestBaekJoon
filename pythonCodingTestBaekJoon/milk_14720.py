# 14720 우유 축제

# 딸기우유(0) -> 초코우유(1) -> 바나나우유(2) -> 딸기우유(0)

N = int(input()) # 우유 가게 개수
milk = list(map(int, input().split()))

count = 0 # 찾은 우유 가게 개수
cur_milk = 0 # 현재 찾으려는 우유가게 순서(0 부터 시작)

for i in range(N):
    if milk[i] == cur_milk:
        count += 1 # 찾은 가게 수 추가
        cur_milk = (cur_milk + 1) % 3 # 0 1 2 순회 하므로 3 으로 나눈 나머지로 다음 순서 가게 설정

print(count) # 최종 방문한 가게 수 출력
