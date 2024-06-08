# 1292 쉽게 푸는 문제

# 1부터 1씩 증가하면서 그 정수 만큼 리스트 요소로 채워짐
# 작은 리스트 먼저 만들고, 빈 리스트에 모두 추가하는 것으로 떠올림
# 정수 A, B(1 ≤ A ≤ B ≤ 1,000) -> 구간의 시작과 끝을 나타내는 정수

A, B = map(int, input().split())
sequence_list = []

def put_same_number(i):
    element_list = [i] * i
    return element_list
# print(put_same_number(3)) # [3, 3, 3]

for i in range(1000):
    sequence_list.extend(put_same_number(i))
# range(5) 일 때 -> print(sequence_list) # [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]

def from_A_to_B_sum(A, B):
    sum = 0
    # sequence_list[A-1] ~ sequence_list[B-1] 합 구하기
    if A <= B:
        for i in range(A-1, B):
            sum += sequence_list[i]
        return sum

print(from_A_to_B_sum(A, B))

# 파이썬 [i] * i 구문은 먼저 [i]로 리스트를 만든 다음, 이 리스트를 i번 반복하여 확장합니다.
# 즉, i의 값이 리스트의 각 요소로 i번 반복되는 새로운 리스트를 생성합니다.

# 리스트1.extend(리스트2) -> 기존 리스트1의 변경
# 리스트1 + 리스트2 -> 새로운 리스트 생성
