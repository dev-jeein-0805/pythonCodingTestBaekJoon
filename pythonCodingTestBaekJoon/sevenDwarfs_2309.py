# 2309 일곱 난쟁이

# 입력 받은 9개의 숫자 중 7개의 합이 100

# 랜덤 추출 7개 할 수 있는 함수가 없는지 먼저 생각이 떠오름
# 구글링 통해 random.choice() 를 먼저 알게 되었으나, 중복 추출이 되는 문제점 발생
# 이후 챗 gpt(뤼튼) 십분 이용하여.. 아래 2가지 라이브러리로 사용하는 방식 배움

import random

heightList = []
for _ in range(9):
    height = int(input())
    heightList.append(height)

# 성공할 때까지 무한 반복
while True:
    newSevenList = random.sample(heightList, 7)  # 중복 없이 7개 선택
    if sum(newSevenList) == 100:
        newSevenList.sort() # 오름차순 정렬
        break  # 올바른 조합을 찾으면 반복 종료

for i in newSevenList:
    print(i)

# 메모리 : 39632KB	/ 시간: 64ms / 언어: Python 3 

# random.sample() => 중복을 허용하지 않음


# ==========================================================================

import itertools

heightList = []
for _ in range(9):
    height = int(input())
    heightList.append(height)

# 9명 중 7명을 선택하는 모든 조합 확인
newSevenList = []
for combination in itertools.combinations(heightList, 7):
    if sum(combination) == 100:
        for height in combination:
            newSevenList.append(height)
            newSevenList.sort()
        break  # 조건을 만족하는 첫 번째 조합을 찾으면 반복 종료

for i in newSevenList:
    print(i)

# 메모리 : 31120KB	/ 시간: 40ms / 언어: Python 3 

# random.choice()를 사용하여 무작위로 키를 선택하는 방식은 중복을 허용함
# itertools.combinations => 모든 가능한 조합을 확인
