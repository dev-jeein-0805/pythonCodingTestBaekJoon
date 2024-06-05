# 7567 그릇

from collections import deque

# 입력 받는 그릇 문자
input_plates = input()
deck = deque(input_plates)

# 최초 그릇의 높이 => 10으로 했더니 5씩 많게 나와서 강제로 줄임. 하지만 이해 안됨..
height = 5

while len(deck) > 1:
        # 앞에서 부터 2개 요소 순차적으로 제거해서 a, b에 저장
        a = deck.popleft()
        b = deck.popleft()
        # 같은 방향
        if a == b:
            height += 5
        # 다른 방향
        else:
            height += 10
        # 뒤에 요소와 비교를 위해 다시 b 맨 앞에 추가
        deck.appendleft(b)
        # 중요! 아래 마지막 1개 남았을 때 비교를 위해 변수에 저장
        last_before_plate = b

if len(deck) == 1:
    # 맨 마지막 요소 제거해서 저장
    last_plate = deck.popleft()
    # 위에 직전 요소랑 마지막 요소 비교
    if last_plate == last_before_plate:
        height += 5
    else:
        height += 10

print(height)
