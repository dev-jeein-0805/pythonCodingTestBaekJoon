# 28417 스케이트보드

# N : 첫째 줄 / 사람 수
# 리스트 7개 요소 중 앞에 2개 슬라이싱 -> 둘 중 최대값 추출 (런)
# 리스트 7 개 요소 중 앞에 2개 제외 5개 슬라이싱 -> 최대값 1,2순위 추출 (트릭)
# 각 줄 마다 3개 요소 더하기
# N 개 줄의 각 최댓값 총합 중 제일 큰 값 최종 출력

N = int(input())

# 마지막에 각 선수의 점수 담을 리스트
eachScoreTotal_list = []

for _ in range(N):
    # 1인 기준 7개 점수 list 로 받아 오기
    score = list(map(int, input().split()))

    # run 점수 (앞에 2개 요소) 슬라이싱
    run = score[:2]
    run_max = max(score[:2])

    # trick 점수 (앞에 2개 요소 제외하고 뒤에 나머지 모두) 슬라이싱
    trick = score[2:]
    # 오름차순 정렬
    trick.sort()
    # 가장 뒤에 있는 거 총 2개 pop 함수로 빼오기
    first_max_trick = trick.pop()
    second_max_trick = trick.pop()

    # run 에서 최고 점수 1개 + trick 에서 최고 점수 2개 모두 더하기
    eachScoreTotal = run_max + first_max_trick + second_max_trick
    # print(eachScoreTotal)
    eachScoreTotal_list.append(eachScoreTotal)

print(max(eachScoreTotal_list))
