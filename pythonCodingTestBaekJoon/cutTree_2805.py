# 2805 나무 자르기

# 절단기 높이 : H
# 문제 : H 최댓값 출력
# 첫번째 줄 : N (나무 수) M (가져가야되는 나무 길이)
# 두번째 줄 : N개의 나무들의 각 높이 (공백으로 구분)

N, M = map(int, input().split())
for _ in range(N):
    height = list(map(int, input().split()))
    print(height)

# 이분탐색 코드 작성 연습 필요
