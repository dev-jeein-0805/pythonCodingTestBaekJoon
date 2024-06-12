# 2798 블랙잭

from itertools import combinations

N, M = map(int, input().split())
cards = list(map(int, input().split()))

max_num = 0 # 최댓값 저장할 변수 초기화

for case in combinations(cards, 3): # cards 에서 중복 없는 조합 3개씩 추출
    case_sum = sum(case) # 각 3개의 합
    if case_sum <= M:
        max_num = max(max_num, case_sum) # 두 값 중 큰 값 반환

print(max_num)
