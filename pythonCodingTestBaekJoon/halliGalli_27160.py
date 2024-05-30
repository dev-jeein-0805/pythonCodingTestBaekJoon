# 딕셔너리 (JS 의 객체 같은 개념!?) 담는 연습

# 입력 받을 플레이어 수
numOfCard = int(input())
# 각 과일 별 총 합한 개수 딕셔너리로 초기화
fruit_counts = {'STRAWBERRY': 0, 'BANANA': 0, 'LIME': 0, 'PLUM': 0}

# 입력 받은 플레이어 수 만큼 입력 값(fruit, num) 받음
for _ in range(numOfCard):
    fruit, num = input().split()
    num = int(num)

    # 입력된 과일의 수를 해당 과일 이름의 key 의 value에 누적해서 더함
    if fruit in fruit_counts:
        fruit_counts[fruit] += num

# 누적된 개수가 업데이트된 fruits_counts 의 값 추출
for count in fruit_counts.values():
    if count == 5:
        print("YES")
        break
else:
    print("NO")

# for 문으로 원하는 값으로 딕셔너리를 업데이트 한 다음에,
# 다시 for 문으로 추출하는 것, 파이썬의 들여쓰기(indented block) 적응이 어려웠다.
# 딕셔너리 관련 함수 : keys() / values() / items() 익히기
